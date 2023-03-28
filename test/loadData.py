import pandas as pd

from test.dataclass import Site


def load_data():
    df = pd.read_csv('sites.csv')
    sites = []
    for i, row in df.iterrows():
        site = Site(row['Name'], row['Backend'], row['Frontend'], row['Popularity'])
        sites.append(site)
    return sites
