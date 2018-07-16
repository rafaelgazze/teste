from app.rules.ruleviolation import RuleViolation

class FirstTransaction90PercentLimit(RuleViolation):
    
    @classmethod
    def check(self, *args):
        account = args[0]
        transaction = args[1]
        lastTransactions = args[2]


        if  len(lastTransactions) == 0 and account.limit * 0.9 < transaction.amount:
            return RuleViolation("First transaction above 90%")
