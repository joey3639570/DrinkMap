import numpy as np
import pandas as pd

def dummy(low,high):
    d = {'DRINK': ['black_tea','bool_h'], 'PRICE': [low, high], 'STORE_NAME': ['mr.wish','50blue'], 'STORE_ADDRESS': ['qqq','www'], 'STORE_PHONE': ['0XX','0XX1']}
    df = pd.DataFrame(data=d)
    return df