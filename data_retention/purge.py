from typing import List

import os
import logging
from .retentionpolicy import RetentionPolicy
from utils.helper import generate_id

logger = logging.getLogger(__name__)


class Purge:
    def __init__(self) -> None:
        self.policies: list[RetentionPolicy] = []
        self.purge_id: str = generate_id()

    def add_policy(self, policy: List) -> None:
        self.policies.extend(policy)
        logging.info(
            f"Added {[policy.policy_name for policy in self.policies]} to the list of policies.")

    def apply_policy(self, folder_name: str, policy: RetentionPolicy) -> None:
        directory = os.fsencode(folder_name)
        logging.info(
            f"Applying policy {policy.policy_name} to folder {folder_name}")
        for file in os.listdir(directory):
            file_path = os.path.join(directory, file)
            policy.check_policy(file_path)
