import pandas as pd

import json
import csv
import os
from tqdm import tqdm


for thn in [2020,2021,2022,2023]:
    path = f'dataset/{thn}/density'
    files =  os.listdir(path)
    for file in tqdm(files):
        filename = os.path.splitext(file)[0]
        df = pd.read_json(os.path.join(path, file))
        df.to_excel(f'export/{thn}/density/{filename}.xlsx', index=False)
    