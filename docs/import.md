To import a function from app/modules/db.py into app/tests/test-db-connection.py, you'll need to follow a few key steps:

1. Ensure Proper Python Module Structure:

    - The app/ directory already has an __init__.py file, making it a Python package.
    - Similarly, the modules/ and tests/ directories also contain __init__.py files, so they can be imported as modules.

2. Update the PYTHONPATH if Necessary:
    -  When running tests or scripts, you need to ensure Python can find the app package. 
      This might mean adjusting the PYTHONPATH environment variable if running outside the project root.
      In this project the root will be query-counties-data
      
      amaseghe@the-eagle:~/developer/python/query-countries-data$ export PYTHONPATH=.

    - This ensures that Python treats the current directory (.) as part of the module search path, making the app package importable.

    $ python3 -m app.tests.test-db-connection
Connected to MySQL Server
MySQL connection is closed
{'id': 1, 'country': 'Kenya', 'capital': 'Nairobi', 'leader': 'William Ruto'}
{'id': 2, 'country': 'Tanzania', 'capital': 'Dodoma', 'leader': 'Samia Suluhu'}
{'id': 3, 'country': 'Uganda', 'capital': 'Kampala', 'leader': 'Yoweri Museveni'}
{'id': 4, 'country': 'Australia', 'capital': 'Canberra', 'leader': 'Anthony Albanese'}
{'id': 5, 'country': 'USA', 'capital': 'Washington', 'leader': 'Joe Biden'}
{'id': 6, 'country': 'South Africa', 'capital': 'Pretoria', 'leader': 'Cyril Ramaphosa'}


3. Import the Function
   - In test-db-connection.py, you should be able to import functions from modules/db.py by using relative imports from the app package.
   
     from app.modules.db import db_querry

4. Run the Command: From the root of your project directory, run:
   - m is module option
   $ python3 -m app.tests.test-db-connection
