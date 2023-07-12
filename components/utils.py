from geopy.geocoders import Nominatim
#import matplotlib.pyplot as plt

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
        
    # def get_color(row, max):
        # cmap = plt.cm.get_cmap('RdYlGn')
        # norm_quantity = row['TotalQuantity'] / max
        # color = cmap(norm_quantity)
        # return [int(c * 255) for c in color]

