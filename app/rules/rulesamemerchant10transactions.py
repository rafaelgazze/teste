from app.rules.ruleviolation import RuleViolation
import json

class More10TransactionsSameMerchant(RuleViolation):

    @classmethod
    def check(self, *args):
        transaction = args[1]
        lastTransactions = args[2]

        count = sum(x.merchant == transaction.merchant for x in lastTransactions)
        
        if count > 10:
            return RuleViolation("More 10 transaction with same merchant")