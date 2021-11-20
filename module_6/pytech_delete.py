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
print("\n --Displaying the student documents from 'find'() query--\n")

# looping through the collection and outputing the results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# inserting 1 student document

Pamela = {
    "student_id": "1010",
    "first_name": "Pamela",
    "last_name": "Sanders",
    "enrollments": [
        {
            "term": "SU22",
            "gpa": 3.80,
            "start_date": "5/24/22",
            "end_date": "8/20/22",
            "courses": [
                {
                    "course_id": "CSD310",
                    "course_description": "Databases",
                    "instructor": "Professor Shelanskey",
                    "grade": "A"
                },
                {
                    "course_id": "CSD330",
                    "course_description": "Java",
                    "instructor": "Professor Payne",
                    "grade": "A" 
                }
            ]   
        },
        {
            "term": "FA22",
            "gpa": "NA",
            "start_date": "8/28/22",
            "end_date": "12/22/22",
            "courses": [
                {
                    "course_id": "CSD330",
                    "course_description": "Web Interfaces",
                    "instructor": "Professor Shelanskey",
                    "grade": "NA"
                },
                {
                    "course_id": "CSD340",
                    "course_description": "Intermediate Java",
                    "instructor": "Professor Payne",
                    "grade": "NA" 
                }
            ]   
        }
    ]
}

# insert statements with output 
print("\n  -- INSERT STATEMENTS --\n")
pamela_student_id = students.insert_one(Pamela).inserted_id
print("  Inserted student record Pamela Sanders into the students collection with document_id " + str(pamela_student_id))

# using student_id to find a student
pamela = students.find_one({"student_id": "1010"})

# outputing the results of find_one
print("\n --Displaying student document from 'find_one()' query --\n")
print(" Student ID: " + pamela["student_id"] + "\n First Name: " + pamela["first_name"] + "\n Last Name: " + pamela["last_name"] + "\n")

# finding the students in the list
student_list = students.find({})

# display message 
print("\n --Displaying the student documents from 'find'() query--\n")

# looping through the collection and outputing the results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# using student_id to delete a student
db.students.delete_one({"student_id": "1010"})

# finding the students in the list
student_list = students.find({})

# display message 
print("\n --Displaying the student documents from 'find'() query--\n")

# looping through the collection and outputing the results
for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# # finding the students in the list
# student_list = students.find({})

# # display message 
# print("\n --Displaying the student documents from 'find'() query--")

# # looping through the collection and outputing the results
# for doc in student_list:
#     print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")