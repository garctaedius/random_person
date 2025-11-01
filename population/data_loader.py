import rasterio
from numpy import ndarray
from affine import Affine

import pickle

def load_population_data() -> tuple[ndarray, Affine]:
    cache_file_location = "population\\cache.pkl"
    
    # Try loading from cache if available
    try:
        with open(cache_file_location, "rb") as cache_file:
            data, transform = pickle.load(cache_file)

    except:
        with rasterio.open("data/global_pop_2025_CN_1km_R2025A_UA_v1.tif") as src:
            data = src.read(1)  # read population count array (on level 1)
            transform = src.transform  # maps pixel coords -> lat/lon

        with open(cache_file_location, "wb") as cache_file:
            pickle.dump((data, transform), cache_file)

    return data, transform