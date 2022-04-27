import os
import random
import string
import logging
from datetime import datetime


logger = logging.getLogger(__name__)


def path_is_valid(path: str) -> bool:
    return os.path.exists(path)


def path_type(path: str) -> str:
    if os.path.isfile(path):
        logging.debug(f"{path} is a file.")
        return "file"

    elif os.path.isdir(path):
        logging.debug(f"{path} is a folder.")
        return "folder"

    else:
        logging.warning(f"{path} is an unknown type.")
        return "unknown"


def convert_bytes_to_kb(size_in_bytes: int) -> int:
    return int(size_in_bytes/1024)


def generate_id() -> str:
    return "".join(random.choices(
        string.ascii_uppercase + string.digits, k=12))


def todays_date() -> str:
    today = datetime.date(datetime.now())
    return today
