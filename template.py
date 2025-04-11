import os
from pathlib import Path
import logging
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

list_files = [
    "src/__iniy__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "trial.ipynb",
    "test.py"
]

for file in list_files:
    file = Path(file)
    filedir, filename = os.path.split(file)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory, {filedir} for the file : {filename}")

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, "w") as f:
            pass
        logging.info(f"creating empty file: {file}")

    else:
        logging.info(f"{filename} already exists")