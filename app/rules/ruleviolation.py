class RuleViolation(object):
    def __init__(self, reason):
        self.reason = reason
        
    def check(self, *args):
        raise NotImplementedError()
