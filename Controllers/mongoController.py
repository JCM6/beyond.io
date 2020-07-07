import pymongo as mongo

mongoUserCredentials = ["sakeUser", "pythonISSNAKE2020"]
mongoDbList = []

"""
client = pymongo.MongoClient("mongodb+srv://snakeUser:<password>@cluster0.cpocf.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.test

Replace <password> with the password for the snakeUser user. 
Replace <dbname> with the name of the database that connections will use by default. Ensure any option params are URL encoded.

"""

connectionString = "mongodb+srv://snakeUser:" + str(mongoUserCredentials[0]) + "@cluster0.cpocf.mongodb.net/"+str(mongoUserCredentials[1]) + "?retryWrites=true&w=majority"
client = mongo.MongoClient(connectionString)
db = client["TestDb"]
collection = db["defaultCardsRaw"]
print(collection)