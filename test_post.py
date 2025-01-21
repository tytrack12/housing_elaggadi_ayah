import requests

url = "http://127.0.0.1:8000/houses"
data = {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "median_house_value": 452600.0,
    "ocean_proximity": "NEAR BAY"
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response JSON:", response.json())