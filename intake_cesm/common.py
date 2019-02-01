import os

import numpy as np
import pandas as pd

from .config import collections


def open_collection(collection):
    """ Open a CESM collection and return a Pandas dataframe """
    try:

        df = pd.read_csv(collections[collection], index_col=0)
        return df

    except (KeyError, FileNotFoundError) as err:
        print("****** The specified collection does not exit. ******")
        raise err


def get_subset(collection, query):
    """ Get a subset of collection entries that match a query """
    df = open_collection(collection)

    condition = np.ones(len(df), dtype=bool)

    for key, val in query.items():
        if not isinstance(val, list) and val is not None:
            val = [val]
            condition = condition & (df[key].isin(val))

    query_results = df.loc[condition].sort_values(
        by=["sequence_order", "files"], ascending=True
    )

    return query_results