import logging

from data_retention.purge import Purge
from data_retention.clients import F24Client
from data_retention.retentionpolicies import (OlderThanOneMonth,
                                              FileLargerThanOneMb)

from website import create_app

from utils.helper import todays_date

logging.basicConfig(filename=f'logs/log_{todays_date()}.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S')


def run_purge():

    # get_client()
    client = F24Client(
        client_id="B49FD014-DBDC-4358-9E31-45BFBD1EBFF0",
        client_name="F24",
        base_folder="C:/force24/Force24_Data_Loop/Adam",
        sub_folders=["", "Folder1", "Folder2", "Folder3"],
        retention_policies=[OlderThanOneMonth(), FileLargerThanOneMb()]
    )
    logging.info(f"process client {client.client_name}.")
    # create purge object

    purge = Purge()

    logging.info(f"Purge object created with id: {purge.purge_id}")

    purge.add_policy(client.retention_policies)

    for folder in client.folder_list:
        for policy in purge.policies:
            purge.apply_policy(folder, policy)
            logging.info(
                f"Applied policy {policy.policy_name} to folder {folder}")

    # delete files
    for policy in purge.policies:
        logging.info(f"Deleting files for policy {policy.policy_name}")
        policy.delete_files()
        logging.info(
            f"{policy.policy_name} file deletion complete.")

    logging.info(f"Purge {purge.purge_id} completed.")
    logging.info(f"{client.client_name} client completed.")


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
