# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, USER, PASS): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'NeoIsTheOne' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)
                return result.acknowledged
            except Exception as error:
                print("Create operation failed:", error)
                return False
        else:
            raise Exception(
                "Nothing to save, because data parameter is empty"
            )

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            try:
                results = self.database.animals.find(data)

                # The find() method returns a MongoDB cursor.
                # Convert the cursor into a list before returning it.
                return list(results)

            except Exception as error:
                print("Read operation failed:", error)
                return []
        else:
            raise Exception(
                "Nothing to search, because data parameter is empty"
            )
            
    # Update method to implement the U in CRUD.
    def update(self, query, new_data):
        if query is not None and new_data is not None:
            try:
                # $set changes only the fields included in new_data.
                result = self.database.animals.update_many(
                    query,
                    {"$set": new_data}
                )

                return result.modified_count

            except Exception as error:
                print("Update operation failed:", error)
                return 0
        else:
            raise Exception(
                "Nothing to update, because query or new_data parameter is empty"
            )

    # Delete method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            try:
                result = self.database.animals.delete_many(data)

                return result.deleted_count

            except Exception as error:
                print("Delete operation failed:", error)
                return 0
        else:
            raise Exception(
                "Nothing to delete, because data parameter is empty"
            )