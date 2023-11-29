# used to create the project structure 
# a real template to create the proj structure for the end-to-end project

import os
import sys
from pathlib import Path
import logging

# first write logging screen (to generate logs)
# only log the INFO level, then the format gives the current
# time of the execution, and the message
logging.basicConfig(
    level=logging.INFO, 
    format='[%(asctime)s]: %(message)s')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py", #constructor required for the local libraries used during the project
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    # the path needs to be defined to work for Windows
    # the paths are originally written in Linux format (forward slash)
    # we need something that transforms them to Windows format
    # that's the Path() method
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "": #if the folder is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # if the filepath does not exist or the file does not contain anything, then:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        # if there's an existing file already
        logging.info(f"{filename} is already created!")