import pytest
from app.account import Account
from app.transaction import Transaction

from app.rules.rulefirsttransaction import FirstTransaction90PercentLimit
from app.rules.ruleviolation import RuleViolation

def test_FirstTransactionAbove90percent():
    input = {
        "Account": {
            "cardIsActive": True,
            "limit": 100,
            "blacklist": ["Abc1234","Cielo"],
            "isWhielisted": True
        },
        "Transaction":{
            "merchant": "Abc1234",
            "amount": 95,
            "time": "2018-07-15 09:01:50"
        }
    }

    account = Account(input.get("Account"))
    transaction = Transaction(input.get("Transaction"))

    assert FirstTransaction90PercentLimit(RuleViolation).check(account,transaction, []) is not None

def test_FirstTransactionBelow90percent():
    input = {
        "Account": {
            "cardIsActive": True,
            "limit": 100,
            "blacklist": ["Abc1234","Cielo"],
            "isWhielisted": True
        },
        "Transaction":{
            "merchant": "Abc1234",
            "amount": 75,
            "time": "2018-07-15 09:01:50"
        }
    }

    account = Account(input.get("Account"))    
    transaction = Transaction(input.get("Transaction"))

    assert FirstTransaction90PercentLimit(RuleViolation).check(account,transaction, []) is None


def test_FirstTransactionBelow90percentWithLastTransactions():
    input = {
        "Account": {
            "cardIsActive": True,
            "limit": 100,
            "blacklist": ["Abc1234","Cielo"],
            "isWhielisted": True
        },
        "Transaction":{
            "merchant": "Abc1234",
            "amount": 75,
            "time": "2018-07-15 09:01:50"
        },
        "LastTransactions": [{
            "merchant": "Abc123",
            "amount": 100,
            "time": "2018-07-15 09:01:00"
        }]
     
    }

    account = Account(input.get("Account"))    
    transaction = Transaction(input.get("Transaction"))
    lastTransactions = []
    [lastTransactions.append(Transaction(transaction)) for transaction in input.get("LastTransactions")]

    assert FirstTransaction90PercentLimit(RuleViolation).check(account,transaction, lastTransactions) is None

