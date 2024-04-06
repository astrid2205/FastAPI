# FastAPI coding exercise

You may test the API using the [Interactive API docs](https://fastapi-n8ag.onrender.com/docs) or try it out on my [React app](https://tinghsuan.onrender.com/).

## Generate password

### API Endpoint:

- URL: [https://fastapi-n8ag.onrender.com/generate-password](https://fastapi-n8ag.onrender.com/generate-password)
- Method: `POST`

### Request Payload:

A JSON payload containing fields for password generation, with default values using security best practices, which contains a password length of 12, including lowercase letters, uppercase letters, numbers, and special characters.

```json
{
  "length": 12,
  "allow_upper": true,
  "allow_number": true,
  "allow_special": true
}
```

The user has the option not to use certain groups of characters, but lowercase letters are always included.

### Password generator logic:

The first few letters are randomly chosen from each group of characters to ensure that every group exists at least once in the password. The rest of the password, each character is randomly selected from the randomly chosen group.

The password generated is between the length of 8 to 30.

### Response:

Returns a JSON response with the generated password and the length of the password.

```json
{
  "password": "U1%cp(C(-J-4",
  "length": 12
}
```

### Error Handling:

Input type is defined in the schema, and FastAPI automatically returns error messages regarding input type errors.

Users trying to request a password with an invalid length will result in an error.

## Custom API endpoint (Recommend restaurant)

Given a location, recommend a restaurant of `categories`
with travel `mode` within `time_range`, and return the route from the start location to the destination restaurant.

For example, recommend a Chinese restaurant within walking distance of 15 mins from the British Museum.

### API Endpoint:

- URL: https://fastapi-n8ag.onrender.com/recommend-restaurant?REQUEST_PARAMS

- Method: `GET`

### Request parameters:

| Name       | Format | Description                                                                                                                                                                              | Example                     |
| ---------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| location   | string | Address / place name to search                                                                                                                                                           | british museum              |
| mode       | string | Travel mode <br>(walk / bus / bicycle)                                                                                                                                                   | walk                        |
| time_range | int    | Time (in minutes) <br>default is 15                                                                                                                                                      | 15                          |
| categories | string | Type of the restaurant <br>(full list in the [API doc](https://fastapi-n8ag.onrender.com/docs#/default/recommend_restaurant_recommend_restaurant_get))<br>default is catering.restaurant | catering.restaurant.chinese |

example: https://fastapi-n8ag.onrender.com/recommend-restaurant?location=british%20museum&mode=walk&time_range=15&categories=catering.restaurant.chinese

### Third-party API Integration:

I used [Geoapify](https://apidocs.geoapify.com/):

- [Geocoding API](https://apidocs.geoapify.com/docs/geocoding/forward-geocoding/#about) for getting the geocode (latitude, longitude) of the location.

- [Isolines API](https://apidocs.geoapify.com/docs/isolines/) to get the isochrone geometry range.

- [Places API](https://apidocs.geoapify.com/docs/places/) to get the restaurants with input categories within the geometry range.

- [Routing API](https://apidocs.geoapify.com/playground/routing/) to generate GeoJSON route from the start location to the destination restaurant.

### Response:

Return a JSON response containing data mostly from Routing API. The response also contains some information about the start and destination.

```json
{
  "features": [
    {
      "type": "Feature",
      "properties": {
        "mode": "walk",
        "waypoints": [
          {
            "location": [-0.128017, 51.519293],
            "original_index": 0
          },
          {
            "location": [-0.12918, 51.517228],
            "original_index": 1
          }
        ],
        "units": "metric",
        "distance": 500,
        "distance_units": "meters",
        "time": 562.072,
        "legs": [
          {
            "distance": 500,
            "time": 562.072,
            "steps": [
              {
                "from_index": 0,
                "to_index": 6,
                "distance": 127,
                "time": 133.962,
                "instruction": {
                  "text": "Walk southeast on the walkway."
                }
              },
              {
                "from_index": 6,
                "to_index": 7,
                "distance": 5,
                "time": 4.39,
                "instruction": {
                  "text": "Continue."
                }
              }
            ]
          }
        ]
      },
      "geometry": {
        "type": "MultiLineString",
        "coordinates": [
          [
            [-0.127509, 51.519447],
            [-0.127128, 51.519122]
          ]
        ]
      },
      "start": {
        "name": "British Museum",
        "address": "British Museum, Great Russell Street, London, WC1B 3DG, United Kingdom",
        "lat": 51.51929365,
        "lon": -0.12801772178494725
      },
      "destination": {
        "name": "Dalloway Terrace",
        "address": "Dalloway Terrace, 16-22 Great Russell Street, London, WC1B 3NN, United Kingdom",
        "lon": -0.1291801,
        "lat": 51.5172283
      }
    }
  ],
  "properties": {
    "mode": "walk",
    "waypoints": [
      {
        "lat": 51.51929365,
        "lon": -0.12801772178494725
      },
      {
        "lat": 51.5172283,
        "lon": -0.1291801
      }
    ],
    "units": "metric"
  },
  "type": "FeatureCollection"
}
```

If no restaurant is found within the range, the response will only include the information of the start location.

```json
{
  "start": {
    "name": "British Museum",
    "address": "British Museum, Great Russell Street, London, WC1B 3DG, United Kingdom",
    "lat": 51.51929365,
    "lon": -0.12801772178494725
  },
  "destination": "No restaurant found."
}
```

Error messages will be shown if the start location is not found, or any other issues during retriving data from Geoapify API.

```json
{
  "detail": "Failed to retrieve data from geoapify."
}
```
