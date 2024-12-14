
import pandas as pd
from  extract import extract
from  transform import transform
from  load import load

test_data = extract('data/product_info.csv')
dataframe = transform(test_data)
print(dataframe)
load(dataframe)



