 
import requests
import json
from pandas import json_normalize

# Define the URL
url = "https://randomuser.me/api"

  
response = requests.get(url)

response_json = json.loads(response.text)
json_format = response_json['results'][0]

processed_user=json_normalize({
        'firstname':json_format['name']['first'],
        'lastname':json_format['name']['last'],
        'country':json_format['location']['country'],
        'username':json_format['login']['username'],
        'password':json_format['login']['password'],
        'email':json_format['email']
    })

print(processed_user)