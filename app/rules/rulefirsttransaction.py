from app.rules.ruleviolation import RuleViolation

class FirstTransaction90PercentLimit(RuleViolation):
    def check(self, account, transaction, lastTransactions):
        if  len(lastTransactions) == 0 and account.limit * 0.9 < transaction.amount:
            return RuleViolation("First transaction above 90%")
