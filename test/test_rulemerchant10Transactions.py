import pytest
from app.account import Account
from app.transaction import Transaction
from app.rules.rulesmerchant10transactions import More10TransactionsSameMerchant
from app.rules.ruleviolation import RuleViolation

def test_MerchantInMore10Transactions():
    input = {
        "Account": {
            "cardIsActive": True,
            "limit": 100,
            "blacklist": ["Abc1234","Cielo"],
            "isWhielisted": True
        },
        "Transaction":{
            "merchant": "Abc1234",
            "amount": 101,
            "time": "2018-07-15 09:01:50"
        },
        "LastTransactions":[
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            },
            {
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
            }
        ]
    }
    account = Account(input.get("Account"))
    transaction = Transaction(input.get("Transaction"))
    lastTransactions = []
    [lastTransactions.append(Transaction(transaction)) for transaction in input.get("LastTransactions")]

    assert More10TransactionsSameMerchant(RuleViolation).check(account, transaction, lastTransactions) is not None
    

def test_Below10TransactionsInSameMerchant():
    input = {
        "Account": {
            "cardIsActive": True,
            "limit": 200,
            "blacklist": ["Abc12345","Cielo"],
            "isWhielisted": True
        },
        "Transaction":{
            "merchant": "Abc1234",
            "amount": 101,
            "time": "2018-07-15 09:01:50"
        },
        "LastTransactions":[{
                "merchant": "Abc1234",
                "amount": 101,
                "time": "2018-07-15 09:01:50"
        }]
    }
    account = Account(input.get("Account"))
    transaction = Transaction(input.get("Transaction"))
    lastTransactions = []
    [lastTransactions.append(Transaction(transaction)) for transaction in input.get("LastTransactions")]
    
    assert More10TransactionsSameMerchant(RuleViolation).check(account, transaction, lastTransactions) is None


