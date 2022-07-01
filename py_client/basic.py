import requests

# endpoints ="https://httpbin.org/anything"
endpoints = "http://127.0.0.1:8000/"

"""To make a request we need to use the requests library and using the get method"""

"""
A Regular HTTP Requets gives us an HTML Response
A REST API HTTP Request gives us a JSON Response
"""

"""Emulates a http GET request"""
# get_response = requests.get(endpoints) 

"""Passing in our json data into the http get request"""
# get_response = requests.get(endpoints, json={"query": "Hello World"})
get_response = requests.get(endpoints)


"""prints a json response"""
print(get_response.text)

"""prints a python dictionary-like object"""
# print(get_response.json())

"""prints the status code of the response"""
print(get_response.status_code)
