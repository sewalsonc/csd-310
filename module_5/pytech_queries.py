# inporting method
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

# using student_id to find a student
cammy = students.find_one({"student_id": "1008"})

# outputing the results of find_one
print("\n --Displaying student document from 'find_one()' query --")
print(" Student ID: " + cammy["student_id"] + "\n First Name: " + cammy["first_name"] + "\n Last Name: " + cammy["last_name"] + "\n")

input("\n\n End of program, press any key to continue...")