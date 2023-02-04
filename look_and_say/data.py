import os
from pathlib import Path
from datetime import datetime

import pandas as pd

ROOT_DIR: Path = Path(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR: Path = ROOT_DIR / 'data'


def save_to_csv(data: dict):
    df = pd.DataFrame(data)

    name = datetime.now().strftime('%Y_%m_%d_%H:%M') + '.csv'
    full_path = DATA_DIR / name

    df.to_csv(full_path)
