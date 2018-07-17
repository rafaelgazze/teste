from app.rules.ruleblacklistmerchant import MerchantBlackList
from app.rules.rulecardblocked import CardBlocked 
from app.rules.rulelimit import LimitAboveTransaction 
from app.rules.rulefirsttransaction import FirstTransaction90PercentLimit
from app.rules.rulesmerchant10transactions import More10TransactionsSameMerchant
from app.rules.ruletwominutestransactions import More3Transactions2MinutesInterval


rules = []
rules.append(MerchantBlackList)
rules.append(CardBlocked)
rules.append(FirstTransaction90PercentLimit)
rules.append(LimitAboveTransaction)
rules.append(More10TransactionsSameMerchant)
rules.append(More3Transactions2MinutesInterval)


class Transaction:
    def __init__(self, transactionJson):
        self.merchant = transactionJson.get('merchant')
        self.amount = transactionJson.get('amount')
        self.time = transactionJson.get('time')    
    
    @staticmethod
    def get_invalidation_rules(account, transaction, lastTransactions):
        rulesViolation = []
        for rule in rules:
            ruleViolation = rule.check(account, transaction, lastTransactions)
            if ruleViolation is not None:
                rulesViolation.append(ruleViolation)
            
        return rulesViolation

