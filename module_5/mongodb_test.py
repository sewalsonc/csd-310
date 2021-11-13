# inporting method
from pymongo import MongoClient

# connection to MongoDB
url = "mongodb+srv://admin:admin@cluster0.ausf5.mongodb.net/pytech"

# to connect the cluster in Mongodb
client = MongoClient(url)

# to connect to the pytech database
db = client.pytech

print("\n -- Pytech Collection List --")
print(db.list_collection_names())


input("\n\n End of program, press any key to exit... ")