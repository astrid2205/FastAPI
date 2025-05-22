from enum import Enum
from fastapi import HTTPException
import random
import requests
import os

apiKey = os.getenv('apiKey')

# Accepted travel mode
class TravelMode(str, Enum):
    walk = "walk"
    bicycle = "bicycle"
    bus = "bus"
    drive = "drive"

# A list of restaurant categories
class CateringType(str, Enum):
    restaurant = "catering.restaurant"	
    pizza = "catering.restaurant.pizza"
    burger = "catering.restaurant.burger"
    regional = "catering.restaurant.regional"
    italian = "catering.restaurant.italian"
    chinese = "catering.restaurant.chinese"
    sandwich = "catering.restaurant.sandwich"
    chicken = "catering.restaurant.chicken"
    mexican = "catering.restaurant.mexican"
    japanese = "catering.restaurant.japanese"
    american = "catering.restaurant.american"
    kebab = "catering.restaurant.kebab"
    indian = "catering.restaurant.indian"
    asian = "catering.restaurant.asian"
    sushi = "catering.restaurant.sushi"
    french = "catering.restaurant.french"
    german = "catering.restaurant.german"
    thai = "catering.restaurant.thai"
    greek = "catering.restaurant.greek"
    seafood = "catering.restaurant.seafood"
    fish_and_chips = "catering.restaurant.fish_and_chips"
    steak_house = "catering.restaurant.steak_house"
    international = "catering.restaurant.international"
    tex = "catering.restaurant.tex-mex"
    vietnamese = "catering.restaurant.vietnamese"
    turkish = "catering.restaurant.turkish"
    korean = "catering.restaurant.korean"
    noodle = "catering.restaurant.noodle"
    barbecue = "catering.restaurant.barbecue"
    spanish = "catering.restaurant.spanish"
    fish = "catering.restaurant.fish"
    ramen = "catering.restaurant.ramen"
    mediterranean = "catering.restaurant.mediterranean"
    friture = "catering.restaurant.friture"
    beef_bowl = "catering.restaurant.beef_bowl"
    lebanese = "catering.restaurant.lebanese"
    wings = "catering.restaurant.wings"
    georgian = "catering.restaurant.georgian"
    tapas = "catering.restaurant.tapas"
    indonesian = "catering.restaurant.indonesian"
    arab = "catering.restaurant.arab"
    portuguese = "catering.restaurant.portuguese"
    russian = "catering.restaurant.russian"
    filipino = "catering.restaurant.filipino"
    african = "catering.restaurant.african"
    malaysian = "catering.restaurant.malaysian"
    caribbean = "catering.restaurant.caribbean"
    peruvian = "catering.restaurant.peruvian"
    bavarian = "catering.restaurant.bavarian"
    brazilian = "catering.restaurant.brazilian"
    curry = "catering.restaurant.curry"
    dumpling = "catering.restaurant.dumpling"
    persian = "catering.restaurant.persian"
    argentinian = "catering.restaurant.argentinian"
    oriental = "catering.restaurant.oriental"
    balkan = "catering.restaurant.balkan"
    moroccan = "catering.restaurant.moroccan"
    pita = "catering.restaurant.pita"
    ethiopian = "catering.restaurant.ethiopian"
    taiwanese = "catering.restaurant.taiwanese"
    latin_american = "catering.restaurant.latin_american"
    hawaiian = "catering.restaurant.hawaiian"
    irish = "catering.restaurant.irish"
    austrian = "catering.restaurant.austrian"
    croatian = "catering.restaurant.croatian"
    danish = "catering.restaurant.danish"
    tacos = "catering.restaurant.tacos"
    bolivian = "catering.restaurant.bolivian"
    hungarian = "catering.restaurant.hungarian"
    western = "catering.restaurant.western"
    european = "catering.restaurant.european"
    jamaican = "catering.restaurant.jamaican"
    cuban = "catering.restaurant.cuban"
    soup = "catering.restaurant.soup"
    uzbek = "catering.restaurant.uzbek"
    nepalese = "catering.restaurant.nepalese"
    czech = "catering.restaurant.czech"
    syrian = "catering.restaurant.syrian"
    afghan = "catering.restaurant.afghan"
    malay = "catering.restaurant.malay"
    chili = "catering.restaurant.chili"
    belgian = "catering.restaurant.belgian"
    ukrainian = "catering.restaurant.ukrainian"
    swedish = "catering.restaurant.swedish"
    pakistani = "catering.restaurant.pakistani"
    fast_food = "catering.fast_food"
    salad = "catering.fast_food.salad"
    hot_dog = "catering.fast_food.hot_dog"
    cafe = "catering.cafe"
    waffle = "catering.cafe.waffle"
    coffee_shop = "catering.cafe.coffee_shop"
    donut = "catering.cafe.donut"
    crepe = "catering.cafe.crepe"
    bubble_tea = "catering.cafe.bubble_tea"
    cake = "catering.cafe.cake"
    frozen_yogurt = "catering.cafe.frozen_yogurt"
    dessert = "catering.cafe.dessert"
    coffee = "catering.cafe.coffee"
    tea = "catering.cafe.tea"
    food_court = "catering.food_court"
    bar = "catering.bar"
    pub = "catering.pub"
    ice_cream = "catering.ice_cream"
    biergarten = "catering.biergarten"
    taproom = "catering.taproom"


# Response examples
restaurant_responses = {
    200: {
        "description": "Success",
        "content": {
            "application/json": {
                "examples": {
                    "Success": {"value": 
                                {"features": [ { "type": "Feature", "properties": { "mode": "walk", "waypoints": [ { "location": [ -0.128017, 51.519293 ], "original_index": 0 }, { "location": [ -0.12918, 51.517228 ], "original_index": 1 } ], "units": "metric", "distance": 500, "distance_units": "meters", "time": 562.072, "legs": [ { "distance": 500, "time": 562.072, "steps": [ { "from_index": 0, "to_index": 6, "distance": 127, "time": 133.962, "instruction": { "text": "Walk southeast on the walkway." } }, { "from_index": 6, "to_index": 7, "distance": 5, "time": 4.39, "instruction": { "text": "Continue." } } ] } ] }, "geometry": { "type": "MultiLineString", "coordinates": [ [ [ -0.127509, 51.519447 ], [ -0.127128, 51.519122 ] ] ] }, "start": { "name": "British Museum", "address": "British Museum, Great Russell Street, London, WC1B 3DG, United Kingdom", "lat": 51.51929365, "lon": -0.12801772178494725 }, "destination": { "name": "Dalloway Terrace", "address": "Dalloway Terrace, 16-22 Great Russell Street, London, WC1B 3NN, United Kingdom", "lon": -0.1291801, "lat": 51.5172283 }} ], "properties": { "mode": "walk", "waypoints": [ { "lat": 51.51929365, "lon": -0.12801772178494725 }, { "lat": 51.5172283, "lon": -0.1291801 } ], "units": "metric" }, "type": "FeatureCollection"}},
                    "No restaurant found": {"value": { "start": { "name": "British Museum", "address": "British Museum, Great Russell Street, London, WC1B 3DG, United Kingdom", "lat": 51.51929365, "lon": -0.12801772178494725 }, "destination": "No restaurant found." }}
                }
            }
        },
    },
    422 : {
        "description": "Unprocessable Content",
        "content": {
            "application/json": {
                "examples": {
                    "Geoapify server error": {"value": {"detail": "Failed to retrieve data from geoapify."}},
                    "Location not found": {"value": {"detail": "Location not found."}}
                }
            }
        },
    }
}


def recommend_restaurant(location, mode, time_range, categories):
    """ 
    Given a location, recommend a restaurant of {categories} 
    with travel {mode} within {time_range}. 
    For example, recommend a Chinese restaurant within walking distance of 15 mins from british museum.
    """

    # Get geocode (latitude, longitude) of the location
    url = f"https://api.geoapify.com/v1/geocode/search?text={location}&format=json&apiKey={apiKey}"      
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=422, detail="Failed to retrieve data from geoapify.")
    response = r.json()
    if len(response['results']) == 0: 
        raise HTTPException(status_code=422, detail="Location not found.")
    results = response['results']
    result = ''
    for i in range(len(results)):
        if 'name' in results[i]:
            result = results[i]
            break
    if not result:
        raise HTTPException(status_code=422, detail="Location not found.")
    start = {"name": result['name'], "address": result['formatted'], "lat": result['lat'], "lon": result['lon']}

    # Get isochrone geometry range
    url = f"https://api.geoapify.com/v1/isoline?lat={start['lat']}&lon={start['lon']}&type=time&mode={mode.value}&range={time_range*60}&apiKey={apiKey}"
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=422, detail="Failed to retrieve data from geoapify.")
    response = r.json()
    if len(response['features']) == 0:
        raise HTTPException(status_code=422, detail="Can not generate isochrone map.")
    geometry_id = response['features'][0]['properties']['id']

    # Get restaurants within the geometry range (get up to 20 restaurants and randomly pick one as the destination.)
    cat = []
    for c in categories:
        cat.append(c.value)
    url = f"https://api.geoapify.com/v2/places?categories={','.join(cat)}&filter=geometry:{geometry_id}&bias=proximity:{start['lon']},{start['lat']}&limit=20&apiKey={apiKey}"
          
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=422, detail="Failed to retrieve data from geoapify.")
    response = r.json()
    raw_restaurants = response['features']
    restaurants = []
    if len(raw_restaurants) == 0:
        return {"start": start, "destination": "No restaurant found."}
    for r in raw_restaurants:
        if 'name' in r['properties']:
            restaurants.append({"name": r['properties']['name'], "address": r['properties']['formatted'], "lon": r['properties']['lon'], "lat": r['properties']['lat']})
    destination = random.choice(restaurants)

    # Get the route from the start location to the recommended restaurant
    url = f"https://api.geoapify.com/v1/routing?waypoints={start['lat']},{start['lon']}|{destination['lat']},{destination['lon']}&mode={mode.value}&apiKey={apiKey}"      
    r = requests.get(url)
    if r.status_code != 200:
        raise HTTPException(status_code=422, detail="Failed to retrieve data from geoapify.")
    response = r.json()

    # Add the start location and the recommended restaurant to the response
    response['features'][0]['start'] = start
    response['features'][0]['destination'] = destination

    return response