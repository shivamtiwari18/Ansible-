# import pymongo
import bson
import json

# create a PyMongo client
# client = pymongo.MongoClient()

# specify the database and collection to read from
# db = client['mydatabase']
# collection = db['mycollection']

# read the BSON file into a bytes object
with open('searches.bson', 'rb') as f:
    bson_data = f.read()

# decode the BSON data using PyMongo's BSON module
data = bson.decode_all(bson_data)

# insert the data into the collection
# collection.insert_many(data)
# print(data)


with open('searches.json', 'w') as f:
    json.dump(data, f, indent=4, default=str)


owner_lst = []

for item in data:
    # print()
    owner_lst.append(item['owner'])

owners = [*set(owner_lst)]

print(owners)

# print(data[0]["owner"])

time = []

for i in range(0, len(owners)):
    if owners[i] == data[["owner"]]:
        time.append(data["queries"]["timerange"]["from"])


print(time)


