class Transaction(object):
    def __init__(self, merchant, amount, time):
        self.merchant = merchant
        self.amount = amount
        self.time = time
        self.rules = []
        self.rules.append(object)

    @classmethod
    def isValid(self):
        print('calma ai')
