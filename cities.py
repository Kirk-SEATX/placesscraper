import pandas as pd
import googlemaps
from variables import api_key

my_key = api_key
gmaps = googlemaps.Client(key=my_key)

#import data
city_df = pd.read_csv('city_pop')
#create a small test set
test_batch = city_df.iloc[328:]
#create city_state to pass to geocode
test_batch['city_state'] = test_batch['City'].str.cat(test_batch['ST'], sep=', ')

#create function to get latitude
def get_latitude(city_state):
    result = gmaps.geocode(city_state)
    if result:
        return result[0]['geometry']['location']['lat']
    else:
        return None

#create function to get longitude
def get_longitude(city_state):
    result = gmaps.geocode(city_state)
    if result:
        return result[0]['geometry']['location']['lng']
    else:
        return None

#get test_batch latitude
test_batch['latitude'] = test_batch.apply(lambda row: get_latitude(row['city_state']), axis=1)
#get test_batch longitude
test_batch['longitude'] = test_batch.apply(lambda row: get_longitude(row['city_state']), axis=1)


place_test = gmaps.places_nearby(location='42.652579, -73.756232', radius=5000, keyword='board games', open_now=False)
print(place_test)