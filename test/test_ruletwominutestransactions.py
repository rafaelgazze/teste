import pytest
from app.account import Account
from app.transaction import Transaction
from app.rules.ruletwominutestransactions import More3Transactions2MinutesInterval
from app.rules.ruleviolation import RuleViolation

def test_More3Transactions2MinutesInterval():
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
            "time": "2018-07-15 09:02:00"
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
                "time": "2018-07-15 09:00:20"
            }
        ]
    }
    account = Account(input.get("Account"))
    transaction = Transaction(input.get("Transaction"))
    lastTransactions = []
    [lastTransactions.append(Transaction(transaction)) for transaction in input.get("LastTransactions")]

    assert More3Transactions2MinutesInterval(RuleViolation).check(account, transaction, lastTransactions) is not None


def test_More3TransactionsAbove2MinutesInterval():
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
            "time": "2018-07-15 09:10:00"
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
                "time": "2018-07-15 09:00:20"
            }
        ]
    }
    account = Account(input.get("Account"))
    transaction = Transaction(input.get("Transaction"))
    lastTransactions = []
    [lastTransactions.append(Transaction(transaction)) for transaction in input.get("LastTransactions")]

    assert More3Transactions2MinutesInterval(RuleViolation).check(account, transaction, lastTransactions) is None
    

def test_With2TransactionsOnly():
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
    
    assert More3Transactions2MinutesInterval(RuleViolation).check(account, transaction, lastTransactions) is None


