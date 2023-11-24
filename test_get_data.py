from AppModules.clientModules import *
from AppModules.socketParams import *

# Test
def test_get_kenya():
    query = "get:Kenya"
    results = ClientChat(query).messaging()

    expected_results = '[1, "Kenya", "Nairobi", "William Ruto", "Nabii full of stories. Great runners there!"]'

    assert results == expected_results

def test_get_tanzania():
    query = "get:Tanzania"
    results = ClientChat(query).messaging()

    expected_results = '[5, "Tanzania", "Dodoma", "Salma Suluhu", "Addictive! Too beautiful!"]'
    assert results == expected_results