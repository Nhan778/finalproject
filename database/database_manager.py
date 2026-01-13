from pymongo import MongoClient, DESCENDING
import config
class DatabaseManager: 
    _instance = None 

    def __new__(cls): 
        if cls._instance is None: 
            cls._instance = super(DatabaseManager, cls).__new__(cls) 
            cls._instance._initialize() 
        return cls._instance 
   
    def _initialize(self):
        self.client = MongoClient(config.MONGO_URI) 
        self.db = self.client[config.DATABASE_NAME] 
        try:
           
            self.db.command("ping") 
            
            self._create_index()
            print("Initialize DB successfully!") 
        except Exception as e:
            print(f"Error in connect: {e}")
            raise e

    
    def _create_index(self):
        "Create indexes for better perfomance"
        self.db.transactions.create_index([("user_id",DESCENDING), ("date", DESCENDING)])
        self.db.categories.create_index([("user_id", DESCENDING), ("type", -1), ("name", -1)],
                                        unique = True)    
    

   
    def get_collection(self, collection_name: str):
        return self.db[collection_name] 

    
    def close_connection(self):
        if self.client: 
            self.client.close()
            print("Shutdown DB connection")
        else:
            print("There is no DB connecting!")