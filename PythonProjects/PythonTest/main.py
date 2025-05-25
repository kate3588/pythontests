import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6e67df6973152c1a85b96d6bda7b22b4'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "katerina358897785g@yandex.ru",
    "password": "358897785Katya"} 

body_confirmation = {
    "trainer_token": TOKEN}

body_create = {
    "name": "CAT",
    "photo_id": 12
}


body_change = {
    "pokemon_id": "324824",
    "name": "CAT35",
    "photo_id": 35
}
body_catch = {
    "pokemon_id": "324824"
}



'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

"""response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)"""

"""response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)"""

"""message = response_create.json()['message']
print(message)"""

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)