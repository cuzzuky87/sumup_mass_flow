import pandas as pd
import numpy as np

pd_raw = pd.read_csv('data.csv')
pd_raw['mass_flow'] = pd_raw['velocity'] * pd_raw['area']

pd_center = pd.read_csv('center.csv')
