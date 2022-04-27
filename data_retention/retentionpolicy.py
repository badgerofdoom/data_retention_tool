import logging
from abc import ABC, abstractmethod
import os
from datetime import date, datetime

from utils.helper import path_is_valid, convert_bytes_to_kb, path_type

logger = logging.getLogger(__name__)


class RetentionPolicy(ABC):
    """
    Abstract class for retention policy
    """
    matched_files: list[str] = []

    @abstractmethod
    def check_policy(self):
        pass

    def delete_files(self) -> None:
        if not self.matched_files:
            logging.info(f"No files to delete for policy {self.policy_name}")
            return

        for file in self.matched_files:
            if path_is_valid(file) and path_type(file) == "file":
                logging.warning(f"Deleting file {file}")
                os.remove(file)
                self.matched_files.remove(file)


class TimeBasedPolicy(RetentionPolicy):
    def __init__(self, policy_name: str, max_file_age: date) -> None:
        self.policy_name = policy_name
        self.max_file_age = max_file_age

    def check_policy(self, file_name: str) -> None:
        info = os.stat(file_name)
        age: date = datetime.fromtimestamp(info.st_ctime).date()
        file_type: str = path_type(file_name)
        if age <= self.max_file_age and file_type == "file":
            self.matched_files.append(file_name)
            logger.info(f"{file_name} matched {self.policy_name} policy.")

    def __str__(self) -> str:
        return f"""Policy name: {self.policy_name},
    Maximum file age: {self.max_file_age}."""


class FileSizeBasedPolicy(RetentionPolicy):
    def __init__(self, policy_name: str, max_file_age: date,
                 max_file_size_kb: int) -> None:
        self.policy_name = policy_name
        self.max_file_age = max_file_age
        self.max_file_size_kb = max_file_size_kb

    def check_policy(self, file_name: str) -> None:
        info = os.stat(file_name)
        size_kb: int = convert_bytes_to_kb(info.st_size)
        age: date = datetime.fromtimestamp(info.st_ctime).date()
        file_type: str = path_type(file_name)
        if size_kb >= self.max_file_size_kb and \
                age <= self.max_file_age and \
                file_type == "file":
            self.matched_files.append(file_name)
            logger.info(f"{file_name} matched {self.policy_name} policy.")

    def __str__(self) -> str:
        return f"""Policy name: {self.policy_name},
    Maximum file age: {self.max_file_age},
    Maximum file size KBs: {self.max_file_size_kb}."""


class FolderSizeBasedPolicy(RetentionPolicy):
    def __init__(self, policy_name: str, max_folder_size_kb: int,
                 max_file_age: date,
                 max_file_size_kb: int = 0) -> None:
        self.policy_name = policy_name
        self.max_folder_size_kb = max_folder_size_kb
        self.max_file_age = max_file_age
        self.max_file_size_kb = max_file_size_kb

    def check_policy(self, folder_name: str) -> None:
        info = os.stat(folder_name)
        size_kb = convert_bytes_to_kb(info.st_size)
        age = datetime.fromtimestamp(info.st_ctime).date()
        if size_kb >= self.size_kb and \
            age <= self.file_age and \
                path_type(folder_name) == "folder":
            self.matched_files.append(folder_name)
            logger.info(f"{folder_name} matched {self.policy_name} policy.")

    def __str__(self) -> str:
        return f"""Policy name: {self.policy_name},
    Maximum folder size: {self.max_folder_size_kb},
    Maximum file age: {self.max_file_age},
    Maximum file size KBs: {self.max_file_size_kb}."""
