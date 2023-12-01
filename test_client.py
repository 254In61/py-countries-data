from ClientModules.clientModules import *

# Test
def test_get_kenya():
    query = "get:Kenya"
    results = ClientChat(query).messaging()

    expected_results = '[["Kenya", 254, "Nairobi", "William Ruto", 50.2]]'
    assert results == expected_results

def test_get_uganda():
    query = "get:Uganda"
    results = ClientChat(query).messaging()

    expected_results = '[]'
    assert results == expected_results

def test_get_usa():
    query = "get:USA"
    results = ClientChat(query).messaging()

    expected_results = '[["USA", 1, "Washington", "Joe Biden", 320.4]]'
    assert results == expected_results