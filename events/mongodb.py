
# The functions defined in this file are used to upload/download data to/from MongoDB
import pymongo

client = pymongo.MongoClient()
db = client['project']   # The data is stored in database named 'project' in MongoDB
col = db['weather']   # The data is stored in the collection named 'weather' in 'project' database

# This function inserts data into MongoDB
def upload_data(data):
    col.insert_one(data)
    return

# This function retrieves the last entered data from MongoDB
def download_data():
    cursor = col.find().sort([('_id',-1)]).limit(1)
    data = list(cursor)
    return data[0]
