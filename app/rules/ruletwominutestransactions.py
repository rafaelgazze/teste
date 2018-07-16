from app.rules.ruleviolation import RuleViolation
from datetime import datetime, timedelta

class More3Transactions2MinutesInterval(RuleViolation):

    @classmethod
    def check(self, *args):
        transaction = args[1]
        lastTransactions = args[2]
        datetimeFinal = ''
        if len(lastTransactions) > 1:
            datetimeTransaction = datetime.strptime(transaction.time, "%Y-%m-%d %H:%M:%S")
            
            datetimePenultimateTransaction= datetime.strptime(lastTransactions[1].time, "%Y-%m-%d %H:%M:%S")

            datetimeFinal = timedelta(seconds=datetimeTransaction.timestamp()) - timedelta(seconds=datetimePenultimateTransaction.timestamp())

            if datetimeFinal.seconds / 60 < 2:
                return RuleViolation("2 minutes in 3 transactions")

        
