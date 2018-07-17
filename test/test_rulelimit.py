import pytest
from app.account import Account
from app.transaction import Transaction
from app.rules.rulelimit import LimitAboveTransaction
from app.rules.ruleviolation import RuleViolation

def test_LimitAbove():
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
    }
    account = Account(input.get("Account"))
    transaction = Transaction(input.get("Transaction"))

    assert LimitAboveTransaction(RuleViolation).check(account, transaction) is not None
    

def test_LimitBelow():
    input = {
        "Account": {
            "cardIsActive": True,
            "limit": 200,
            "blacklist": ["Abc1234","Cielo"],
            "isWhielisted": True
        },
        "Transaction":{
            "merchant": "Abc1234",
            "amount": 101,
            "time": "2018-07-15 09:01:50"
        },
    }
    account = Account(input.get("Account"))
    transaction = Transaction(input.get("Transaction"))
    
    assert LimitAboveTransaction(RuleViolation).check(account, transaction) is None
