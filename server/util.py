import json
import pickle
import numpy as np
import pandas as pd

__data_columns = None
__locations = None
__model = None
#1st routine to get location names
def get_location_names() :
    return __locations

#2nd routine
def get_estimated_prices(location, sqft, bhk, bath) :
    try:
        loc_idx = __data_columns.index(location.lower())
    except:
        loc_idx = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[3] = bhk
    if loc_idx >= 0:
        x[loc_idx] = 1
    data = pd.DataFrame([x], columns = __data_columns)
    return round(__model.predict(data)[0], 2)
def load_saved_artifacts() :
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    with open("artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]
    with open("artifacts/house_price_prediction.pickle", 'rb') as m:
        __model = pickle.load(m)
    print("Loading saved artifacts...done")
if __name__ == "__main__" :
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_prices('1st Phase JP Nagar',1000, 2, 2))
    print(get_estimated_prices('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_prices('Indira Nagar',1000, 3, 2))
    print(get_estimated_prices('Indira Nagar',1000, 3, 3))
