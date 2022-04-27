from dataclasses import dataclass, field
import logging

from .retentionpolicy import RetentionPolicy
from utils.helper import path_is_valid


@dataclass
class F24Client:
    client_id: str
    client_name: str
    base_folder: str
    sub_folders: list[str] = field(default_factory=list)
    retention_policies: list[RetentionPolicy] = field(default_factory=list)
    folder_list: list[str] = field(
        init=False, default_factory=list, repr=False)
    invalid_folder_list: list[str] = field(
        init=False, default_factory=list, repr=False)

    def __post_init__(self):
        for sub_folder in self.sub_folders:
            folder = self.base_folder + "/" + sub_folder
            if path_is_valid(folder):
                self.folder_list.append(folder)
            else:
                self.invalid_folder_list.append(folder)
                logging.warning(f"Invalid folder {folder}.")
