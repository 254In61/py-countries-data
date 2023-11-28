Overview
========
- Tool made up of 3 main parts.
- 1) Database : MySQL Database with a table called "countries"
- 2) Server script : Script that runs within the DB Server , which perfoms SQL querries to the DB.
- 3) client end : Client script picks options, and sends a string over the network socket to a listening server. Server translates the string into an SQL query.
- Design obsifucates the DB Server from external environment.

TESTING
========

1) Unittests
-------------
- pytest is used to unit-test the client function which calls on all other functions and classes.No unittesting of server modules.

2) Integration testing
----------------------
- Workflow created in Jenkins server
- Workflow runs the unittest first and when all is good, integration tests next.
- Integration tests are done using Docker containers to simulate customers, who then run a client script with pre-defined data.

docker
=======
- A ready docker image built as per the Dockerfile attached.
- Docker images are created , script run and then destroyed, all within the ansible script, site.yml.

How to Use
==========
- Set environmental variables for that specific subshell for:
  1) MYSQL_USER 
  2) MYSQL_PASSWORD
- Start the server with server.py

MySQL
=====
- The SQL server details are added in AppModule/socketParams.py

- Sample MySQL Table used:

mysql> select * from Countries;
+-------------+-------------+------------+-----------------+-------------------+
| CountryName | CountryCode | Capitol    | Leader          | PopulationMillion |
+-------------+-------------+------------+-----------------+-------------------+
| Kenya       |         254 | Nairobi    | William Ruto    |              50.2 |
| Tanzania    |         255 | Dodoma     | Samia Suluhu    |              60.2 |
| Australia   |          61 | Canberra   | Antony Albanese |              28.5 |
| USA         |           1 | Washington | Joe Biden       |             320.4 |
+-------------+-------------+------------+-----------------+-------------------+
4 rows in set (0.00 sec)

- Ensure your Application Server has python mysql-connector installed.
  $ pip install mysql-connector-python



Author
======
254in61