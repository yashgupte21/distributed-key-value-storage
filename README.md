# distributed-key-value-storage
An empirical evaluation of distributed key value storage systems - MongoDB and Cassandra


---- Cassandra Setup ----
Install Cassandra on all the 8 nodes and configure the configuration files. Add the required IP address of required nodes inside the configuration file.

Execute Cassandra.py on node 1

	time python3 Cassandra.py

The output of the above commands gives us the overall time , Insert , LookUp time and Delete Time


--- Mongo DB setup ---

Install Mongo DB on all the 8 nodes and configure the configuration files. Add the required IP address of required nodes inside the configuration file.

Execute  Mongodb.py on one node

	time python3 Mongodb.py

The output of the above commands gives us the overall time , Insert , LookUp time and Delete Time