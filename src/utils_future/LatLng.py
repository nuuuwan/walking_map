from dataclasses import dataclass


@dataclass
class LatLng:
    lat: float
    lng: float

    @staticmethod
    def from_str(latlng_str: str):
        lat, lng = latlng_str.split(',')
        return LatLng(float(lat), float(lng))

    def __str__(self) -> str:
        return f'{self.lat},{self.lng}'

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def expand(latlng1, latlng2, n_steps: int) -> list:
        dlat, dlng = latlng2.lat - latlng1.lat, latlng2.lng - latlng1.lng
        latlng_list = []
        for i in range(n_steps + 1):
            latlng_list.append(
                LatLng(
                    latlng1.lat + dlat * i / n_steps,
                    latlng1.lng + dlng * i / n_steps,
                )
            )
        return latlng_list
