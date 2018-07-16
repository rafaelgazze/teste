from app.rules.ruleviolation import RuleViolation

class CardBlocked(RuleViolation):
    
    @classmethod
    def check(self, *args):
        account = args[0]
        if not account.cardIsActive:
            return RuleViolation("Card is blocked")
