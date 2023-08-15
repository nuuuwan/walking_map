import sys

from utils_future.GoogleMap import GoogleMap
from utils_future.LatLng import LatLng

if __name__ == '__main__':
    latlng_str_start, latlng_str_end, n_steps_str = sys.argv[1:4]
    n_steps = int(n_steps_str)
    latlng_start = LatLng.from_str(latlng_str_start)
    latlng_end = LatLng.from_str(latlng_str_end)
    google_map = GoogleMap(LatLng.expand(latlng_start, latlng_end, n_steps))
    google_map.open()
