import requests
import json

url_1 = "https://learn-co-curriculum.github.io/json-site-example/"
response_1 = requests.get(url_1)
# print(response_1) # => <Response [200]>
# print(response_1.text)
# printing request text in unicode
# => an html as a unicode string


# set a url to get data
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

# make a GET request to that url
response = requests.get(url)

# print out content in bytes in JSON format in a list
# print(response.content)

# JSON.loads(json_string) parse and convert JSON string into Python dict
json_content = json.loads(response.text)

# JSON.dumps(python_dict) convert python obj into json string
print(json.dumps(json_content, indent=4, sort_keys=True))
