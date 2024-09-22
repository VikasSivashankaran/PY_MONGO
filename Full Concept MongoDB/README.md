What is database?
- Arrangement of Hierarchical structure of data or organizing data in specified directory or folder with folder name

-> It is Object-oriented database which means it posses with key value pair

terminal->1.type ->mongosh
(ensure mongo is installed)

2.type->show dbs
(this shows the database in system if it obtained)

3.type->use appdb
(this is name of database that going to use to store data)

4.type->db.users.insertOne({name:"VIkas"})
(this is the command to create a user with name in json format)

5.type->db.users.find()
fetch the users in database

6.type->db.users.insertMany()
this used to insert more document or data in users' collection

- db.users.find()                                   //display all data
- db.users.find().limit(2)                          //first 2 entries will be displayed using 'limit'
- db.users.find().sort({name:1}).limit(3)           //it sort the name field from alphabet a-z and we can make limit if necessary
- db.users.find().sort({name:-1}).limit(3)          //it sort the name field from z-a when name = -1, this -1 will be sort in reverse the name field 
- db.users.find().sort({age:1,name:-1}).limit(3)     //we can also sort the age from 1 to ......goes on when age is 1
- db.users.find().sort({age:-1,name:1}).limit(3)     // when age is -1 ,it sorts from bigger num to smaller num

- db.users.find().skip(1).limit(2)                // we can also make skip data from out of limit
