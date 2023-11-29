# logging module is defined here instead in a separate module
# just for simplicity!

# It's very important to have a logging module that helps you debug your
# code in a real situation, e.g. running the app in the cloud, where
# there is no terminal, and downloading the logs file can help you
# debug your code

import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")