import pytest
from ServerModules.serverModules import *
# Test CreateQuery class

def test_query_country_pass():
    # Testing query by country name
    # Expected to suceed
    assert DBQuery("get:Kenya").getData() == '[["Kenya", 254, "Nairobi", "William Ruto", 50.2]]'

def test_query_country_fail():
    # Expected to fail
    assert DBQuery("get:Wakanda").getData() == '[["Wakanda", 666, "Space", "Black Panther", 88]]'

