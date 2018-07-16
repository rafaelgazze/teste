from app.rules.ruleviolation import RuleViolation

class MerchantBlackList(self, account, transaction):
    if account.blacklist.contains(transaction.merchant):
        return RuleViolation("Merchant Blacklisted")
