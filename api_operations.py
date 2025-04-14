import json
import os
import random
import requests as rq         
from requests import Response 
from dotenv import load_dotenv

"""
    * Purpose: used to interact with web servers or APIs by sending HTTP requests from Python and handling their responses.

    * Main Role: Acts as (a consumer) a client that makes HTTP requests (GET, POST, etc.) to servers.
 
    * COMMON Functions needed:
        ---------------
        1> .get(), .post(), .put(), .delete() - basics
        2> 

"""

# Initialize global varirables:
base_url: str = 'https://gorest.co.in'

def get_auth_token() -> str | None:
    try:
         load_dotenv()                              # only for local setup, for CI setup, use "GitHub Actions secrets"
         auth_token: str | None = os.getenv('AUTH_TOKEN')
         if not auth_token:                                     # This checks if auth_token is "None" or an "empty string"
              raise ValueError('AUTH_TOKEN environment variable is not set properly')
         return auth_token
    
    except ValueError as error:
         return str(error)

headers: dict[str, str | None] = {
    'Authorization': get_auth_token()
}

# created method to generate unique dictonary each time it runs
def generate_random_payload() -> dict[str, str]:
    # Predefined safe words
    first_names = ['John', 'Emma', 'Michael', 'Sophia', 'David', 'Olivia', 'Robert', 'Ava']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia']

    # Generate random but safe names
    first: str = random.choice(first_names)
    last: str = random.choice(last_names)
    full_name: str = f'{first} {last}'

    # Create email using initials and a random number for uniqueness
    email = f'{first[0].lower()}{last.lower()}{random.randint(100, 999)}@example.com'

    gender: str = random.choice(['male', 'female'])
    status: str = random.choice(['active', 'inactive'])

    # basic payload structure / json schema is set by the Devs, hence any user-defined structure won't work
    # {
    #     'name': 'John Doe',
    #     'email': 'jd23@hotmail.com',
    #     'gender': 'male',
    #     'status': 'active' or 'inactive'
    # }
    payload: dict[str, str] = {
        'name': full_name,
        'email': email,
        'gender': gender,
        'status': status
    }
    return payload


# GET request
def get_request(endpoint_url: str, optional_headers: dict[str, str | None] = {}) -> str:
# NOTE: "optional_headers: dict[str, str | None] = {}" can also be written as "Optional[Dict[str, str | None]] = None"
        try:
            # Validate endpoint_url (simple example)
            if not endpoint_url.startswith('/'):
                return json.dumps({'Error': 'Invalid endpoint format'})
            
            response = rq.get(base_url + endpoint_url,
                              headers = optional_headers,
                              verify = True)                    # Explicitly verify SSL
            # print(base_url + endpoint_url)                    # SECURE - Don't print sensitive info, hence commented
            # print(response.status_code)

            if response.status_code == 200:
                return json.dumps(response.json(), indent = 2)              # the moment we write "json.dumps" it becomes a string and then I'm returning the retrieved response json
            else:
                return json.dumps({'Status code returned': response.status_code, 
                              'Message': 'Request failed'})       
            
        except AssertionError:
            #  return str(f'{type(error).__name__} spotted with the code above')
            # used more SECURE approach would be to return a generic error message that doesn't reveal internal details
            return json.dumps({'Error': 'The Request has failed..', 
                               'Status': 'Error'})
        

# POST request - should return the "id" of user in "int" format
def post_request(endpoint_url: str, payload: dict[str, str]) -> int:
    response: Response = rq.post(base_url + endpoint_url,
                                 headers = headers,
                                 json = payload)
    assert response.status_code == 201
    # print(response.json()['name'], 'should be', payload['name'])
    assert response.json()['name'] == payload['name']
    return int(response.json()['id'])                           # returning the user_id


# PUT request
def put_request(endpoint_url: str, payload: dict[str, str], user_id: int) -> str:
    response: Response = rq.put(base_url + endpoint_url + f'/{user_id}',
                                headers = headers,
                                json = payload)
    assert response.status_code == 200
    # print(response.json()['id'], 'should be', user_id)
    assert response.json()['id'] == user_id
    return json.dumps(response.json(), indent = 2)               # returning the updated response json


# DELETE request
def delete_request(endpoint_url: str, user_id: int) -> Response:
    response: Response = rq.delete(base_url + endpoint_url + f'/{user_id}',
                                   headers = headers)
    assert response.status_code == 204
    return response



# define the endpoint & call the functions
common_endpoint: str = '/public/v2/users'

print('GET call without auth_token: ', 
      get_request(common_endpoint), '\n')

# make a POST call to the API and get the user-id
user_id: int = post_request(common_endpoint, 
                            generate_random_payload())

print('POST call, user created with id: ', 
      user_id, '\n')

print('GET call with auth_token to fetch the recently created user: ', 
      get_request(f'{common_endpoint}/{user_id}',
                  headers), '\n')

print('PUT call: ',
      put_request(common_endpoint, generate_random_payload(), user_id), '\n')


print('DELETE call: ', 
      delete_request(common_endpoint, user_id))

