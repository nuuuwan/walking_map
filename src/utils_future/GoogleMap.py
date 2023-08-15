import webbrowser

from utils_future.LatLng import LatLng


class GoogleMap:
    def __init__(self, latlng_list: list[LatLng]):
        self.latlng_list = latlng_list

    @property
    def url(self) -> str:
        latlng_list_str = '/'.join(
            map(lambda latlng: str(latlng), self.latlng_list)
        )
        return (
            'https://www.google.com/maps/dir'
            + f'/{latlng_list_str}/'
            + 'data=!3m1!4b1!4m2!4m1!3e2'
        )

    def open(self):
        webbrowser.open(self.url)
