- MongoDB Queries

What is database?
- Arrangement of Hierarchical structure of data or organizing data in specified directory or folder with folder name

->Install Mongo Compass and Mongoshell

-> It is Object-oriented database which means it posses with key value pair

terminal->
- mongosh
(ensure mongo is installed)

- show dbs
(this shows the database in system if it obtained)

- use appdb
(this is name of database that going to use to store data)

- db.users.insertOne({name:"VIkas"})
(this is the command to create a user with name in json format)

- db.users.find()
fetch the users in database

- db.users.insertMany()
this used to insert more document or data in users' collection

- db.users.find()                                   //display all data
- db.users.find().limit(2)                          //first 2 entries will be displayed using 'limit'
- db.users.find().sort({name:1}).limit(3)           //it sort the name field from alphabet a-z and we can make limit if necessary
- db.users.find().sort({name:-1}).limit(3)          //it sort the name field from z-a when name = -1, this -1 will be sort in reverse the name field 
- db.users.find().sort({age:1,name:-1}).limit(3)     //we can also sort the age from 1 to ......goes on when age is 1
- db.users.find().sort({age:-1,name:1}).limit(3)     // when age is -1 ,it sorts from bigger num to smaller num

- db.users.find().skip(1).limit(2)                // we can also make skip data from out of limit
- db.users.find({age:21})                        // finds with database whose age is 21

- db.users.find({name:"Vikas"})  //fetch the name 
- db.users.find({name:"Vikas"},{name:1,age:1})
- db.users.insertMany([ {name:"Ramesh", age:19, hobbies:["Singing"],address:{street:"Rameshst",city:"Texas"},balance:100,debt:200}, {name:"Suresh", age:44, hobbies:["Gaming"],address:{street:"Sureshst",city:"Coimbatore"},balance:20,debt:0}])

- Complex Queries

- db.users.find({name:{$eq:"Ramesh"}})   // eq means equal to

- db.users.find({name:{$ne:"Ramesh"}})  //ne means not equal to

- db.users.find({age:{$gt:25}}) // gt means greater than
- db.users.find({age:{$gte:25}}) //gte means greater than equal to

- db.users.find({age:{$lt:21}})
- db.users.find({age:{$lte:21}}) // code for less than and less than equal to

- db.users.find({name:{$in:["Ramesh","Suresh"]}}) // this checks the name of particular person in its field
- db.users.find({name:{$nin:["Ramesh","Suresh"]}}) // this checks the name of particular person in its field

- db.users.find({age:{$exists:true}}) // this query will give data having age field

- db.users.find({age:{$exists:false}})// data with no age field

- db.users.insertOne({age:null,debt:2000,balance:10})
- db.users.find({age:{$gte:20,$lte:40}})

- db.users.find({age:{$gte:20,$lte:40},name:"Vikas"})//from age 20 to 40 name Vikas the value can get

- db.users.find({$and:[{age:21},{name:"Vikas"}]})//AND operation
- db.users.find({$or:[{age:21},{name:"Vikas"}]})//or operation
-  db.users.find({age:{$lte:25}}) 
- db.users.find({age:{$not:{$lte:25}}})
- db.users.find({$expr:{$gt:["debt","balance"]}})//making comparision using "expr"
- db.users.find({$expr:{$gt:["$debt","$balance"]}})
- db.users.find({"address.city":"Texas"})//fetch data where city is texas

- db.users.findOne({$expr:{$gt:["$debt","$balance"]}})

- db.users.countDocuments({$expr:{$gt:["$debt","$balance"]}})
- db.users.countDocuments({age:{$gte:21}})


- Update Queries

- db.users.updateOne({age:44},{$set:{age:34}})
- db.users.find({age:34})

- db.users.updateOne({_id:ObjectId('66efb2f04679fbdde6c73bf9')},{$set:{name:"Balakumar"}})

- db.users.find({_id:ObjectId('66efb2f04679fbdde6c73bf9')})

- db.users.updateOne({_id:ObjectId('66efb2f04679fbdde6c73bf9')},{$inc:{age:3}})//increment the age by 3

- db.users.updateOne({_id:ObjectId('66efb2f04679fbdde6c73bf9')},{$rename:{balance:"remainingBalance"}})//rename
- db.users.find({_id:ObjectId('66efb2f04679fbdde6c73bf9')})
- db.users.updateOne({_id:ObjectId('66efb2f04679fbdde6c73bf9')},{$push:{hobbies:"Clapping"}})//pushing new hobby
- db.users.updateOne({_id:ObjectId('66efb2f04679fbdde6c73bf9')},{$pull:{hobbies:"Dancing"}})// pull one hobby
- db.users.updateOne({_id:ObjectId('66efb2f04679fbdde6c73bf9')},{$unset:{age:""}})
- db.users.updateMany({address:{$exists:true}},{$unset:{address:""}})// deletes all address
 
- db.users.find()
- db.users.replaceOne({age:19},{name:"sivaa_in"})

- db.users.deleteOne({debt:2000})
- db.users.deleteMany({age:{$exists:false}})
- show collections