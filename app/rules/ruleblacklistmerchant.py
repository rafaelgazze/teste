from app.rules.ruleviolation import RuleViolation

class MerchantBlackList(RuleViolation):
    
    @classmethod
    def check(self, *args):
        account = args[0]
        transaction = args[1]
        
        if transaction.merchant in account.blacklist:
            return RuleViolation("Merchant Blacklisted")
