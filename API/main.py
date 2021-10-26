import datetime
import time

from schedule import every, repeat, run_pending
from ingestors import DaySummaryIngestor
from writes import DataWriter

ingestor = DaySummaryIngestor(
    writer=DataWriter,
    coins=["BTC", "ETH", "LTC"],
    default_start_date=datetime.date(2021, 10, 1),
)


@repeat(every(1).seconds)
def Job():
    ingestor.ingest()


while True:
    run_pending()
    time.sleep(0.5)
