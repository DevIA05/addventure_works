from geopy.geocoders import Nominatim

# Fonction pour obtenir les coordonnées
class Geocoder:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="GeoLoc")

    def get_coordinates(self, country):
        loc = self.geolocator.geocode(country)
        if loc:
            return loc.latitude, loc.longitude
        else:
            return None, None

