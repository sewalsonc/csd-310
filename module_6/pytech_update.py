# inporting method
from typing import Set
from pymongo import MongoClient

# connection to MongoDB
url = "mongodb+srv://admin:admin@cluster0.ausf5.mongodb.net/pytech"

# to connect the cluster in Mongodb
client = MongoClient(url)

# to connect to the pytech database
db = client.pytech

# get the student collection
students = db.students

# finding the students in the list
student_list = students.find({})

# display message 
print("\n --Displaying the student documents from 'find'() query--")

# looping through the collection and outputing the results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

print()

db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Bower"}})

print()

x = students.find_one({"student_id": "1007"})
print(x)
