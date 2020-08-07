import pandas as pd
import os

path = "./data/"

for filename in os.listdir(path):
    if filename.endswith(".csv"):
        csv = pd.read_csv(os.path.join(path, filename))
        continue
    else:
        continue
