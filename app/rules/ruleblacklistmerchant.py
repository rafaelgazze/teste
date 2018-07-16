from app.rules.ruleviolation import RuleViolation

class MerchantBlackList(RuleViolation):
    def check(self, transaction, account):
        if transaction.merchant in account.blacklist:
            return RuleViolation("Merchant Blacklisted")
