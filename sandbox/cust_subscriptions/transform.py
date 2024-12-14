import pandas as pd
import numpy

def transform(data):
    t_data = data
    t_data.columns = [x.upper() for x in t_data.columns]
    t_data = t_data.drop_duplicates()
    t_data.reset_index(drop=True, inplace=True)
    print(f"\n Out of {data.shape[0]} records, only {t_data.shape[0]} records remain after data cleaning. \n\n")
    return t_data 
