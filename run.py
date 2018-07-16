from app.transaction import Transaction
from app.account import Account
import json

input  = {
  "Account": {
    "cardIsActive": True,
    "limit": 100,
    "blacklist": ["Aaaaa","Cielo"],
    "isWhielisted": True
  },
  "Transaction":{
    "merchant": "Abc123",
    "amount": 110,
    "time": "2018-07-15 09:01:50"
  },
  "LastTransactions": [
    {
      "merchant": "Abc1234",
      "amount": 100,
      "time": "2018-07-15 09:01:00"
    },
    {
      "merchant": "Abc1234",
      "amount": 100,
      "time": "2018-07-15 09:00:00"
    }
  ]
}

account = Account(input.get("Account"))
transaction = Transaction(input.get("Transaction"))
lastTransactions = []
[lastTransactions.append(Transaction(transaction)) for transaction in input.get("LastTransactions")]

rulesViolation = Transaction.get_invalidation_rules(account,transaction,lastTransactions)

if len(rulesViolation) > 0:
    rules = ','.join(str(rule.reason) for rule in rulesViolation)
    print (json.dumps({'approved': False, 'newLimit': account.limit, 'deniedReasons': ','.join(str(rule.reason) for rule in rulesViolation)}))
else:
    print (json.dumps({'approved': True, 'newLimit': (account.limit - transaction.amount), 'deniedReasons': None}))




