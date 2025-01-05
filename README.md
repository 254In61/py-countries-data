# Overview
Project end objective is for clients to query data from their end devices and get the info they want.

Private project in a Private repo.

# design
- Data stored in a mysql db server.
- mysql db server hosted in a kubernetes cluster as a pod.
- application server has the logic.
- Client does a query on Web browser or uses curl.

# mysql db & k8s cluster
- Microk8s cluster is installed on the-eagle(192.168.1.100).

- The-eagle is also the application server and has access to the K8s cluster that hosts the myql app.

- Check svc details attached to the pod:
  $ kubectl get svc  OR  $ kubectl describe svc/mysql

- Test access: $ mysql -h <cluster Ip assigned to mysql> -P 3306 -u panther -p
  Example: mysql -h 10.152.183.178 -P 3306 -u panther -p

# testing application server
1. - On the-eagle : $ cd app/tests && python3 test-server.py

  $ python3 test-server.py 
 * Serving Flask app 'test-server'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.100:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 105-246-364

2. - From remote clients send https requests either through 
   a) web browser
   b) curl : $ curl http://192.168.1.100:5000/hello
   c) postman
 - 3 end-points have been created for the test-server.py i.e /mambo, /malagho and /hello
 - Send requests to these end-points.

# dns names
- I don't have a DNS at home.
- But I have the following in /etc/hosts


# testing db connection
1. log into the-eagle

2. confirm the mysql svc ip first and confirm it is the one in ~/secrets/mysql-microk8s-env-vars-the-eagle
   $ kubectl get svc  OR  $ kubectl describe svc/mysql

3. $ git clone repo or $ git pull if already existing and in need of update.

4. $ source ~/secrets/mysql-microk8s-env-vars-the-eagle

5. $ python3 test-db-connection.py

# container testing
- Chose to use podman instead of docker because of this :

  permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/create?fromImage=ubuntu&tag=latest": dial unix /var/run/docker.sock: connect: permission denied


# how to use



# author

Name: 254In61