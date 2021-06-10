import numpy as np
import pandas as pd

def dummy(low,high):
    d = {'DRINK': ['black_tea','bool_h'], 'PRICE': [low, high], 'STORE_NAME': ['mr.wish','50blue'], 'STORE_ADDRESS': ['qqq','www'], 'STORE_PHONE': ['0XX','0XX1']}
    df = pd.DataFrame(data=d)
    return df

def dummy_storeq(number):
    d = {'drinkname': ['black_tea','green_tea'], 'drinktype': ['a01','a02'], 'cost': [number, 5]}
    df = pd.DataFrame(data=d)
    return df

def dummy_drink_revise(input_dict):
    d = input_dict
    #print(d)
    df = pd.DataFrame(list(d.items()))
    return df
    
def dummy_store_list():
    return [1,2,3,4,5]