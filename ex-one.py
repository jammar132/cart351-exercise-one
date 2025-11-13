import requests
token = "0b289faf9b3f11e526ad6a022dc301371f6faa49" # my api key
url = "https://api.waqi.info/search/" # url
response = requests.get(url, params={"token": token, "keyword": "montreal"}) # make the request to access results with api key and city
results = response.json() # get the response as json

# 5c.Code to access the content associated with the data field
responseData = results['data']; # Save results from the expression variable called responseData

# 5g. Print out the air quality index for each item AND the uid for each item.
for item in responseData:
    station_info = item["station"]  
    station_name = station_info["name"]
    geo = station_info["geo"]
    latitude = geo[0]
    longitude = geo[1]

    aqi = item["aqi"]                # air quality index
    uid = item["uid"]                # unique station id

    # Neatly labelled output
    print("Station:", station_name)
    print("lat:", latitude)
    print("long:", longitude)
    print("UID:", uid)
    print("AQI:", aqi)
    print("-" * 40)  # separator for readability