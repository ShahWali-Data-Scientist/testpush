import pymongo
client = pymongo.MongoClient("mongodb+srv://shahwalieng1:mongodb1234@cluster0.2hnsigb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db.client.test
print(db)

d = {
    "name":"ShahWali",
    "email":"shahwalieng",
    "surename":"Wali"
}
db1 = client['mongodbtest']
coll = db1['test']
coll.insert_one(d)

