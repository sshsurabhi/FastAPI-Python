Evaluation Render Preview


Review
Introduction to Python Programming for DevOps
In this exam, you will be asked to test your knowledge and apply it in the context of a new concept: APIs.

The exercise will consist of using Python to collect data from the OpenWeatherMap API allowing to retrieve meteorological data via HTTP queries.

Exercise: retrieving data from the OpenWeatherMap API
An HTTP request is made to a URI (Universal Resource Identifier) address consisting of the protocol used ("http://"), a domain name ("domain-name.com") as well as an endpoint ("endpoint"), giving the URI: "http://nom-domaine.com/endpoint".

To retrieve data from an HTTP API, we will use a GET request. There are other types of requests, which will be seen later in the course.

With Python, we can make a GET request using the requests library:

# Import the library
import requests

# Definition of the endpoint to request
endpoint = "http://nom-domaine.com/endpoint"

# Execute the request and store the response of the request
response = requests.get(endpoint)
We can add arguments to a request to authenticate to the API, and also to specify the response that is expected.

For example, we will use the endpoint "https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}" by replacing {CITY_NAME} with a city name and {API_KEY} with a key that will allow us to authenticate to Open Weather Map to access the data.

Import the requests library.

Make a GET request on the endpoint "https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}" by replacing :

{CITY_NAME} by "paris"
{API_KEY} by "18bce6654cb928cd47eccf2abc2b673b"
Store the result of the query in a variable named response.

# Insert your code here
import requests

CITY_NAME = "paris"
API_KEY = "18bce6654cb928cd47eccf2abc2b673b"

endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}" # replacing API_KEY, CITY_NAME in this f string

response = requests.get(endpoint)

print(response.json())
{'coord': {'lon': 2.3488, 'lat': 48.8534}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 294.29, 'feels_like': 294.21, 'temp_min': 293.47, 'temp_max': 295.25, 'pressure': 1018, 'humidity': 67}, 'visibility': 10000, 'wind': {'speed': 5.14, 'deg': 40}, 'clouds': {'all': 100}, 'dt': 1718813485, 'sys': {'type': 2, 'id': 2012208, 'country': 'FR', 'sunrise': 1718768802, 'sunset': 1718827040}, 'timezone': 7200, 'id': 2988507, 'name': 'Paris', 'cod': 200}
The OpenWeatherMap data API will return a JSON file whose structure is identical to that of a Python dictionary. We can display the JSON content of the response using the json method of the response object we obtained.

# Displaying the content of the response
print(response.json())

{'coord': {'lon': 2.3488, 'lat': 48.8534},
 'weather': [{'id': 800,
   'main': 'Clear',
   'description': 'clear sky',
   'icon': '01d'}],
 ...
 ...
 'name': 'Paris',
 'cod': 200}
Define a function named get_city_data taking as argument a city name and returning the content of the response from the OpenWeatherMap API for that city in dictionary form.

Iterate over the list ['paris', 'london', 'washington'] and retrieve the weather data associated with each of these cities. We will store all the answers in a dictionary list named results.

# Insert your code here
import requests

endpoint_ = "https://api.openweathermap.org/data/2.5/weather"
api_keyy = "18bce6654cb928cd47eccf2abc2b673b"

def get_city_data(city):
    end_point = f"{endpoint_}?q={city}&appid={api_keyy}"
    response = requests.get(end_point)
    return response.json()

cities = ['paris', 'london', 'washington']

results = [get_city_data(i) for i in cities]

for j in results:
    print(j)
{'coord': {'lon': 2.3488, 'lat': 48.8534}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 294.18, 'feels_like': 294.09, 'temp_min': 293.36, 'temp_max': 295.25, 'pressure': 1018, 'humidity': 67}, 'visibility': 10000, 'wind': {'speed': 5.14, 'deg': 70}, 'clouds': {'all': 100}, 'dt': 1718814031, 'sys': {'type': 2, 'id': 2012208, 'country': 'FR', 'sunrise': 1718768802, 'sunset': 1718827040}, 'timezone': 7200, 'id': 2988507, 'name': 'Paris', 'cod': 200}
{'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 292.82, 'feels_like': 292.38, 'temp_min': 290.84, 'temp_max': 294.4, 'pressure': 1022, 'humidity': 59}, 'visibility': 10000, 'wind': {'speed': 6.69, 'deg': 100}, 'clouds': {'all': 75}, 'dt': 1718813678, 'sys': {'type': 2, 'id': 2093698, 'country': 'GB', 'sunrise': 1718768569, 'sunset': 1718828461}, 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}
{'coord': {'lon': -120.5015, 'lat': 47.5001}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 289.34, 'feels_like': 288.32, 'temp_min': 287.37, 'temp_max': 291.13, 'pressure': 1018, 'humidity': 50, 'sea_level': 1018, 'grnd_level': 934}, 'visibility': 10000, 'wind': {'speed': 1.46, 'deg': 67, 'gust': 1.13}, 'clouds': {'all': 3}, 'dt': 1718813990, 'sys': {'type': 2, 'id': 2019804, 'country': 'US', 'sunrise': 1718798667, 'sunset': 1718856152}, 'timezone': -25200, 'id': 5815135, 'name': 'Washington', 'cod': 200}
Exercise: Data Processing
By displaying one of the items in the results list, identify the key containing the temperature reading in Kelvin as well as the key indicating the city name.

Define a function named get_city_temp which must take a city name as argument and return the temperature and the city name in the form of a dictionary {"Name" : "City name", "Temperature" : Temperature reading}. You can use the get_city_data function again.

Iterate over the list ['paris', 'london', 'washington'] and display the temperatures of each city. Determine which city is colder.

# Insert your code here
import requests

endpoint_ = "https://api.openweathermap.org/data/2.5/weather"
api_keyy = "18bce6654cb928cd47eccf2abc2b673b"

def get_city_temp(city):
    end_point = f"{endpoint_}?q={city}&appid={api_keyy}"
    response = requests.get(end_point)
    data = response.json()
    temp = data['main']['temp']    
    return {"Name": city, "Temperature": temp}

cities = ['paris', 'london', 'washington']

city_temps = [get_city_temp(i) for i in cities]

for j in city_temps:
    print(f"City: {j['Name']}, Temperature: {j['Temperature']}K")

colder_city = min(city_temps, key=lambda x: x['Temperature'])
print(f"The coldest city is {colder_city['Name']} with a temperature of {colder_city['Temperature']}K")
City: paris, Temperature: 294.18K
City: london, Temperature: 292.82K
City: washington, Temperature: 289.34K
The coldest city is washington with a temperature of 289.34K
Exercise: Code Improvement
When we work on a program or an API, it is important to anticipate and make explicit the errors that our application might encounter.

In our case and especially for automation purposes, we would like to know if our API always returns the expected response.

An HTTP API returns a response but also a status code indicating if the request was successful. Here are some examples of status codes:

200: Means that the request was successful.

40X: Means that the request was not successful due to an error on the part of the client (you).

50X: Means that the request did not succeed because of a server error.

We can check the status code of a request using the status_code attribute of the object returned by the request.

print(response.status_code)
>>> 200
# The request was successful
```
Re-define the get_city_data function to include a condition that will check the status code of the response and display :

"Successful Request." if the status code is 200.
Client Error." if the status code is between 400 (included) and 500 (excluded).
Server Error." if the status code is between 500 (included) and 600 (excluded).
In addition, if the request is unsuccessful, the function should return None.

Test the get_city_data function with the "paris" argument and the "jdieijdei" argument.

# Insert your code here
endpoint_ = "https://api.openweathermap.org/data/2.5/weather"
api_keyy = "18bce6654cb928cd47eccf2abc2b673b"

def get_city_data(city):
    end_point = f"{endpoint_}?q={city}&appid={api_keyy}"
    response = requests.get(end_point)
    
    if response.status_code == 200:
        print("Successful Request.")
        return
    elif 400 <= response.status_code < 500:
        print("Client Error.")
    elif 500 <= response.status_code < 600:
        print("Server Error.")
    else:
        return None

print(get_city_data("paris"))
print(get_city_data("jdieijdei"))
Successful Request.
None
Client Error.
None
Now we want to interrupt the program and return an error message when the API is not working. For this we will use the sys library and its exit function:

import sys

number = 1

if number < 2 :
sys.exit("The number is less than 2.")

>>> An exception has occurred, use %tb to see the full traceback.
>>>
>>> SystemExit: The number is less than 2.
```
Re-define the get_city_data function to terminate the program when the status code returned by the API is not good. The error message should be the same as in the previous question, but in the form of a SystemExit error.

Test the get_city_data function with the "paris" argument and then the "jdieijdei" argument.

# Insert your code here
import requests
import sys

endpoint_ = "https://api.openweathermap.org/data/2.5/weather"
api_keyy = "18bce6654cb928cd47eccf2abc2b673b"

def get_city_data(city):
    end_point = f"{endpoint_}?q={city}&appid={api_keyy}"
    response = requests.get(end_point)
    
    if response.status_code == 200:
        print("Successful Request.")
        return response.json()

    elif 400 <= response.status_code < 500:
        sys.exit("Client Error.")
    elif 500 <= response.status_code < 600:
        sys.exit("Server Error.")
    else:
        return None

print(get_city_data("paris"))
print(get_city_data("jdieijdei"))
Successful Request.
{'coord': {'lon': 2.3488, 'lat': 48.8534}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 294.18, 'feels_like': 294.09, 'temp_min': 293.36, 'temp_max': 295.25, 'pressure': 1018, 'humidity': 67}, 'visibility': 10000, 'wind': {'speed': 5.14, 'deg': 70}, 'clouds': {'all': 100}, 'dt': 1718814031, 'sys': {'type': 2, 'id': 2012208, 'country': 'FR', 'sunrise': 1718768802, 'sunset': 1718827040}, 'timezone': 7200, 'id': 2988507, 'name': 'Paris', 'cod': 200}
An exception has occurred, use %tb to see the full traceback.

SystemExit: Client Error.