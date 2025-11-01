import rasterio

def load_population_data():
    with rasterio.open("data/global_pop_2025_CN_1km_R2025A_UA_v1.tif") as src:
        data = src.read(1)  # read population count array (on level 1)
        transform = src.transform  # maps pixel coords -> lat/lon

    return data, transform