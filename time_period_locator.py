import pandas as pd
import hvplot
import numpy as np


def rolling_10_and_20_day(dataframe):
    rolling_10_day = dataframe.rolling(window=10).mean()
    rolling_20_day = dataframe.rolling(window=20).mean()
    #ax = dataframe.plot(figsize=(25,10))
    #rolling_10_day.plot(ax=ax)
    #rolling_20_day.plot(ax=ax)
    return rolling_10_day, rolling_20_day

























def run():
    """The main function for finding the increasing price dates."""
    btc_close = 
    # Find the rolling averages
    rolling_10,rolling_20 = 