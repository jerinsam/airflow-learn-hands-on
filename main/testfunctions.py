 
import requests

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

# Make the GET request
response = requests.get(url)
 
 
print(response)