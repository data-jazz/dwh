import pandas as pd
import numpy

def extract(file_path):

    #read file into memory
    data = pd.read_csv(file_path)

    #print details about the file
    print(f" Here is some info about the data in {file_path}:")
    print(f"\nThere are {data.shape[0]} rows and {data.shape[1]} columns in this data frame.")
    print(f"\nThe columns in this dataframe take the following types:")

    # print the type of each column
    print(data.dtypes)
    
    #message before returning the dataframe
    print(f"\nTo view the dataframe extracted from {file_path}, display the value returned by this function! \n\n")
    return data 
    