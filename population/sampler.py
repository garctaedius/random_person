import numpy as np
from rasterio.transform import xy
from affine import Affine

from util.named_types import Location

def sample_weighted_location(data: np.ndarray, transform: Affine) -> Location:
    # Mask out negative cells (where no one lives)
    mask = data > 0

    # Get pixel indices of populated pixels
    rows, cols = np.where(mask)

    # Get an array with all valid population counts
    pop = data[mask]

    # Compute sampling probabilities proportional to population
    probabilities = pop / pop.sum()

    # Select a random pixel (wieghted by population)
    pixel_index = np.random.choice(len(pop), p=probabilities)

    row, col = rows[pixel_index], cols[pixel_index]

    lon, lat = xy(transform, row, col)

    loc = Location(latitude=lat, longitude=lon)

    return loc

    