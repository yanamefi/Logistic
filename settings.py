import pymongo
import fastapi
import redis

app = fastapi.FastAPI()


client = pymongo.MongoClient("mongodb+srv://yanamefi:gKAE9hAGHqkVYoCm@cluster0.o22hb.mongodb.net"
                             "/?retryWrites=true&w=majority&appName=Cluster0")

# Access a specific database
user_db = client["Users_db"]
chat_db = client["Chat"]

# Access a collection within the database
customer_db = user_db["customer"]
requests_db = user_db["requests"]
messages_db = chat_db["messages"]

SECRET_KEY = "8plb0vl6-HkU89IU_GMYBKZIfvVmMOIqrFzvtdA0a14"


redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)


site_directory = "128.0.0.1:8000"
