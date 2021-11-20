# inporting method
from pymongo import MongoClient

# connection to MongoDB
url = "mongodb+srv://admin:admin@cluster0.ausf5.mongodb.net/pytech"

# to connect the cluster in Mongodb
client = MongoClient(url)

# to connect to the pytech database
db = client.pytech

# inserting 3 student documents

William = {
    "student_id": "1007",
    "first_name": "William",
    "last_name": "Corey",
    "enrollments": [
        {
            "term": "SU22",
            "gpa": 3.10,
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

Cammy = {
    "student_id": "1008",
    "first_name": "Cammy",
    "last_name": "Kamradt",
    "enrollments": [
        {
            "term": "SU22",
            "gpa": 3.60,
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

Kyle = {
    "student_id": "1009",
    "first_name": "Kyle",
    "last_name": "Kearney",
    "enrollments": [
        {
            "term": "SU22",
            "gpa": 3.00,
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

# get the students collection 
students = db.students

# insert statements with output 
print("\n  -- INSERT STATEMENTS --\n")
william_student_id = students.insert_one(William).inserted_id
print("  Inserted student record William Corey into the students collection with document_id " + str(william_student_id))

cammy_student_id = students.insert_one(Cammy).inserted_id
print("  Inserted student record Cammy Kamradt into the students collection with document_id " + str(cammy_student_id))

kyle_student_id = students.insert_one(Kyle).inserted_id
print("  Inserted student record Kyle Kearney into the students collection with document_id " + str(kyle_student_id))

input("\n\n End of program, press any key to exit... ")