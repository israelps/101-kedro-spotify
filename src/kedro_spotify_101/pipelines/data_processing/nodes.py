from typing import Any, Dict
import pandas as pd



def merge_datasets(song_info: pd.DataFrame, song_metrics: pd.DataFrame, song_popularity: pd.DataFrame) -> pd.DataFrame:
    ds = song_info.join(song_metrics, how='left').join(song_popularity, how='left')
    
    return ds

def preprocess_raw(ds: pd.DataFrame)-> pd.DataFrame:
    data = ds.copy()
    data = data.drop(['artists','name','year'], axis=1)
    data['popularity'] = data['popularity']/100
    return data