import pymongo


class DB:
    def __init__(self):
        # Establish a connection to the MongoDB database using the provided connection string
        # Add your own string in between the brackets, retrieve it from MongoDB
        self.client = pymongo.MongoClient(
            "mongodb+srv://user123:Paarth12345@cluster0.7sgpqhl.mongodb.net/?retryWrites=true&w=majority"
        )
