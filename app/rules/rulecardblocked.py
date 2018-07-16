from app.rules.ruleviolation import RuleViolation

class CardBlocked(RuleViolation):
    def check(self, account):
        if not account.cardIsActive:
            return RuleViolation("Card is blocked")
