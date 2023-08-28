import os
from pathlib import Path
from datetime import datetime

import pandas as pd

def create_csv():
    ROOT_DIR: Path = Path(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR: Path = ROOT_DIR / 'data'

    if not DATA_DIR.exists():
        DATA_DIR.mkdir()

    name = datetime.now().strftime('%Y_%m_%d_%H:%M') + '.csv'
    full_path = DATA_DIR / name

    return full_path


def save_to_csv(data: dict, full_path):
    try:
        # Load existing CSV file if it exists, otherwise create a new DataFrame
        df = pd.read_csv(full_path)
    except FileNotFoundError:
        df = pd.DataFrame()

    new_row = pd.DataFrame(data)
    df = pd.concat([df, new_row], ignore_index=True)


    df.to_csv(full_path, index=False)


