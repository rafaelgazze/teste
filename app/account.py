class Account(object):
    def __init__(self, cardIsActive, limit, blacklist, isWhiteListed):
        self.cardIsActive = cardIsActive
        self.limit = limit
        self.blacklist = blacklist
        self.isWhiteListed =  isWhiteListed



