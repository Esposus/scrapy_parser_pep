import csv
from collections import defaultdict
from datetime import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

HEADERS = ('Статус', 'Количество')
TIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
TOTAL_STATUSES = 'Total'
FILE_NAME = 'status_summary_{datetime}.csv'


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counter = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counter[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        with open(
            self.results_dir / FILE_NAME.format(
                datetime=dt.now().strftime(TIME_FORMAT)
            ),
            mode='w', encoding='utf-8'
        ) as file:
            csv.writer(file).writerows(
                [
                    HEADERS,
                    *self.status_counter.items(),
                    [TOTAL_STATUSES, sum(self.status_counter.values())]
                ]
            )
