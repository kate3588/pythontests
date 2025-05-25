import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '6e67df6973152c1a85b96d6bda7b22b4'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 34023


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params ={'trainer_id' : TRAINER_ID})
    assert  response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params ={'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'CAT35'