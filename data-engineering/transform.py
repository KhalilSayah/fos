import glob
import json

import pandas as pd


def get_all_filenames():
    filenames = glob.glob('raw_data_*.json')
    return filenames

def transform_one_file(filename):
    data = []
    with open(filename,'r') as j:
        d = json.loads(j.read())
        
    cities = list(d.keys())
    for city in cities:
        info = json.loads(d[city])
        data.append({
            "city" :city,
            "latitude":info['latitude'],
            "longitude":info['longitude'],
            "temperature":info['current_weather']['temperature'],
            "time":info['current_weather']['time']
        })
    return data
    

def merge_all_files_in_pandas_df(files):
    df= pd.DataFrame()
    for file in files:
        df = df.append(pd.DataFrame(transform_one_file(file)),ignore_index=True)
        print(file)
    return df

def drop_duplicates(df_):
    df_ = df_.drop_duplicates()
    return df_

def main():
    files = get_all_filenames()
    df = merge_all_files_in_pandas_df(files)
    df = drop_duplicates(df)
    df.to_csv("transformed_data.csv", index=False)


main()