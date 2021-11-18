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