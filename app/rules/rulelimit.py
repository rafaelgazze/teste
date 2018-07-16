from app.rules.ruleviolation import RuleViolation

class LimitAboveTransaction(RuleViolation):
    def check(self, account, transaction):
        if account.limit < transaction.amount:
            return RuleViolation("Limit below transaction")