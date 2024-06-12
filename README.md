# Run code
First you have to create 3 containers in docker in the same network
We name the containers: 
cas1
cas2
cas3

After this step you should create a network named cassandraNet

Once you have created the containers and network you must follow the next steps.

Write the following commands in the docker terminal:

1. python connect_cassandra.py

2. python testgeneral

3. python test1

4. python test2

5. python test3

6. python test4

7. python test5


(To optimize the tests in the database we run >>python casandra_connect between each test)
