 
import requests
import json

# # Process Data
# def _process_user(ti):
#     user = ti.xcom_pull(task_id = 'extract_user')
#     user = user['results'][0]
#     processed_user=json_normalize({
#         'firstname':user['name']['first'],
#         'lastname':user['name']['last'],
#         'country':user['lcoation']['country'],
#         'username':user['login']['username'],
#         'password':user['login']['password'],
#         'email':user['email'],
#     })
#     processed_user.to_csv('/tmp/processed_user.csv',index=None,header=False)


# Define the URL
url = "https://randomuser.me/"


# Correctly define the headers as a dictionary
headers = {
    "Accept": "application/json"  
}

# Make the GET request with the correct headers parameter
response = requests.get(url, headers=headers)

 
# K = json.loads(response.text)


print(response.text) 
# try:
#     response_data = json.loads(response.text)
# except json.JSONDecodeError as e:
#     print(f"JSON decoding error: {e}") 
 