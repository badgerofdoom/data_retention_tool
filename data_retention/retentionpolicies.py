from datetime import timedelta

from .retentionpolicy import TimeBasedPolicy, FileSizeBasedPolicy
from utils.helper import todays_date

today = todays_date()


class OlderThanOneMonth(TimeBasedPolicy):
    def __init__(self):
        super().__init__("Older than one month", today - timedelta(days=30))


class FileLargerThanOneMb(FileSizeBasedPolicy):
    def __init__(self):
        super().__init__("File larger than 1MB",
                         today - timedelta(days=7), 1024)
