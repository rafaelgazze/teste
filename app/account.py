class Account:
    def __init__(self, accountJson):
        self.cardIsActive = accountJson.get('cardIsActive')
        self.limit = accountJson.get('limit')
        self.blacklist = accountJson.get('blacklist')
        self.isWhiteListed =  accountJson.get('isWhiteListed')



