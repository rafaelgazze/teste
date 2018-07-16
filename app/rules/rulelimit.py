from app.rules.ruleviolation import RuleViolation

class LimitAboveTransaction(RuleViolation):
    
    @classmethod
    def check(self, *args):
        account = args[0]
        transaction = args[1]
        
        if account.limit < transaction.amount:
            return RuleViolation("Limit below transaction")