from pymongo.server_api import ServerApi
import pymongo
from bson.objectid import ObjectId # for ObjectId

# Local database
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# mydb = myclient["okul"] # database name
# print(myclient.list_database_names()) # list all databases



# Server database
name = "muhammedkolee"
password = "jbY1hiuSft5FBPQv"
url = f"mongodb+srv://{name}:{password}@cluster0.lgu7o.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

myclient = pymongo.MongoClient(url)

mydb = myclient["okul"]
mycollection = mydb["sinif"] # collection name

# print(myclient.list_database_names()) # list all databases
# print(mydb.list_collection_names()) # list all collections

# ogrenci = {"name": "Ali", "surname": "Yılmaz", "age": 14} # document

# result = mycollection.insert_one(ogrenci) # insert one document
# print(result)
# print(type(result))

# ogrenciler = [
#     {"name": "Ayşe", "surname": "Yılmaz", "age": 15},
#     {"name": "Ali", "surname": "Yılmaz", "age": 14},
#     {"name": "Veli", "surname": "Tahta", "age": 15}, # documents
    # {"name": "Fatma", "surname": "Erol", "age": 13},
    # {"name": "Kemal", "surname": "Kaya", "age": 17},
#     {"name": "Ahmet", "surname": "Taş", "age": 17},
# ]

# mycollection.insert_many(ogrenciler) # insert many documents


# insert documents different fields
# ogrenciler = [
#     {"name": "Fatma", "surname": "Erol", "age": 13, "description": "Fatma is a good student."},
#     {"name": "Kemal", "surname": "Kaya", "age": 17, "class": "11/A"},
# ]

# mycollection.insert_many(ogrenciler) # insert many documents


# print all documents
# for i in mycollection.find():
#     print(i)


# print all documents with specified fields
# for i in mycollection.find({}, {"_id": 0, "name": 1, "surname": 1}):
#     print(i)


# filter also get use in find_one() method
# print all documents with filter
# filter = {"name": "Ali"} # filter
# for i in mycollection.find(filter):
#     print(i)


# find documents with ObjectId 
# filter = {"_id": ObjectId("677172b577702a3dbd27f9bb")}
# print(mycollection.find_one(filter))



# like for 
# result = mycollection.find({
#     "name": {
#         "$in": ["Ali", "Ayşe"] # Ali or Ayşe
#     }
# })
# for i in result:
#     print(i)



# result = mycollection.find({
#     "age": {
#         "$gt": 14 # greater than 14
#     }
# })
# for i in result:
#     print(i)


# result = mycollection.find({
#     "age": {
#         "$lt": 15 # less than 15
#     }
# })
# for i in result:
#     print(i)


# result = mycollection.find({
#     "name": {
#         "$eq": "Ahmet" # equal to Ahmet
#     }
# })
# for i in result:
#     print(i)

# for more operators: https://docs.mongodb.com/manual/reference/operator/query/


# result = mycollection.find().sort("name", -1) # 1 for ascending, -1 for descending
# for i in result:
#     print(i)


# result = mycollection.find().sort([("name", -1), ("surname", 1)]) # first sort by name descending, then sort by surname ascending
# for i in result:
#     print(i)



# update one document
# mycollection.update_one(
#     {"name": "Ayşe"},
#     {
#         "$set": {"name": "Narin"}
#     }
# )
# result = mycollection.find()
# for i in result:
#     print(i)  



# update many documents
# mycollection.update_many(
#     {"name": "Fatma"},
#     {
#         "$set": {"name": "Narin", "surname": "Kara", "age": 17}
#     }
# )
# result = mycollection.find()
# for i in result:
#     print(i)  




# delete one document
# result = mycollection.find()
# for i in result:
#     print(i)

# print("*"*50)

# mycollection.delete_one({"name": "Narin"})

# result = mycollection.find()
# for i in result:
#     print(i)



# delete many documents
# result = mycollection.find()
# for i in result:
#     print(i)

# print("*"*50)

# mycollection.delete_many({"name": "Narin"})

# result = mycollection.find()
# for i in result:
#     print(i)