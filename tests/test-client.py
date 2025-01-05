# Run : $ pytest tests/test-client.py -vvv

import requests

def get_country_details(country):
    url = f"http://192.168.1.100:5000/countries/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()

def test_capital():
    dict_x = get_country_details("Kenya")
    # assert get_country_details("Kenya") == {'capital': 'Nairobi', 'country': 'Kenya', 'id': 1, 'leader': 'William Ruto'}
    assert dict_x['capital'] == 'Nairobi'

def test_none():
    assert get_country_details("Wakanda") == None

def test_leader():
    dict_x = get_country_details("Australia")
    # assert get_country_details("Australia") == {'capital': 'Canberra', 'country': 'Australia', 'id': 4, 'leader': 'Anthony Albanese'}
    assert dict_x['leader'] == 'Anthony Albanese'