from os import stat
from deck import deck
from hand import hand
from strategy_importer import strategy_importer
import numpy

from collections import Counter

HARD_STRATEGY = {} 
SOFT_STRATEGY = {}
PAIR_STRATEGY = {}

importer = strategy_importer('BlackJack\\blackjack_strategy.csv')
HARD_STRATEGY, SOFT_STRATEGY, PAIR_STRATEGY = importer.import_strategy()

d = deck(8)

SIMULATIONS = 1000
INIT_BANKROLL = 100
INIT_AMOUNT = 1

def player_play(hand : hand, dealer_card):
    if len(hand.cards) < 2:
        hand.add_card(d.draw())

    while not hand.busted() and not hand.blackjack():
        if hand.soft():
            flag = SOFT_STRATEGY[hand.soft_value()][str(dealer_card)]
        else:
            flag = HARD_STRATEGY[hand.final_value()][str(dealer_card)]
        
        prob = round(d.probability_of_card_needed(21 - player_hand.final_value()), 2)

        print('Current value: ' + str(hand.final_value()) + ' , probability of not going bust: ' + str(prob))

        if flag == 'D':
            if len(hand.cards) == 2:
                hand.doubled = True
                hand.add_card(d.draw())
                break
            flag = 'H'
        
        if flag == 'Sp':
            #split here#
            if hand.final_value() <= 11:
                flag = 'H'
            else:
                flag = 'S'
        
        if flag == 'H':
            if prob > 50:
                card = d.draw()
                hand.add_card(card)
            else:
                flag = 'S'
        
        if flag == 'S':
            break

def dealer_play(hand : hand):
    while hand.final_value() < 17:
        card = d.draw()
        hand.add_card(card)

wins = 0
bankroll = INIT_BANKROLL
bet = INIT_AMOUNT

for a in range(SIMULATIONS):
    if d.deck_size() < 150:
        d.shuffle()

    bankroll -= bet
    player_hand = hand()
    dealer_hand = hand()

    if bankroll < 0:
        print('BANKRUPT')
        break

    player_hand.add_card(d.draw())
    dealer_hand.add_card(d.draw())
    player_hand.add_card(d.draw())
    dealer_hand.add_card(d.draw())

    player_play(player_hand, dealer_hand.cards[0])
    if not player_hand.blackjack():
        dealer_play(dealer_hand)
    
    status = "PLAY"

    if player_hand.busted():
        status = "LOST"
    else:
        if player_hand.blackjack():
            if dealer_hand.blackjack():
                status = "PUSH"
            else:
                status = "WON"
                winnings = bet * 2.5
        elif dealer_hand.busted():
            status = "WON"
        elif dealer_hand.final_value() < player_hand.final_value():
            status = "WON"
        elif dealer_hand.final_value() > player_hand.final_value():
            status = "LOST"
        elif dealer_hand.final_value() == player_hand.final_value():
            if dealer_hand.blackjack():
                status = "LOST"
            else:
                status = "PUSH"

    if status == "LOST":
        bet*=2
    elif status == "WON":
        wins +=1
        winnings = bet * 2
        if player_hand.doubled:
            bankroll -= bet
            winnings *= 2
        bankroll += winnings
        bet = INIT_AMOUNT
    elif status == "PUSH":
        bankroll += bet
    
    print('Result: ' + status + ', Player Hand: ' + str(player_hand.final_value()) + ', Dealer Hand: ' + str(dealer_hand.final_value()) + ', Doubled?: ' + str(player_hand.doubled) + ', BankRoll: ' + str(bankroll))

print(wins)
print(bankroll)