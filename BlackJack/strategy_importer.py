import csv

class strategy_importer(object):
    hard_strat = {}
    soft_strat = {}
    pair_strat = {}

    def __init__(self, file):
        self.file = file

    def import_strategy(self):
        hard = 21
        soft = 21
        pair = 10

        with open(self.file, 'rU') as file_csv:
            reader = csv.DictReader(file_csv, delimiter = ',')
            for row in reader:
                
                if hard >= 3:
                    self.hard_strat[hard] = row
                    hard -=1
                elif soft >= 12:
                    self.soft_strat[soft] = row
                    soft -=1
                elif pair >= 1:
                    self.pair_strat[pair] = row
                    pair -=1

        return self.hard_strat, self.soft_strat, self.pair_strat

