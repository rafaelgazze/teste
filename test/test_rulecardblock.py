import pytest
from app.account import Account
from app.rules.rulecardblocked import CardBlocked
from app.rules.ruleviolation import RuleViolation

def test_IsNotBlockCard():
    input = {
        "Account": {
            "cardIsActive": True,
            "limit": 100,
            "blacklist": ["Abc1234","Cielo"],
            "isWhielisted": True
        }
    }

    account = Account(input.get("Account"))
    assert CardBlocked(RuleViolation).check(account) is None

def test_IsBlockCard():
    input = {
        "Account": {
            "cardIsActive": False,
            "limit": 100,
            "blacklist": ["Abc1234","Cielo"],
            "isWhielisted": True
        }
    }
    account = Account(input.get("Account"))    
    assert CardBlocked(RuleViolation).check(account) is not None

