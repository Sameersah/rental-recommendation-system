from models import PropertyResponse
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://dev:MongoDBDev@18.119.153.150:27017/dev?directConnection=true&authSource=dev"
DB_NAME = "dev"
COLLECTION_NAME = "sample"

print(f"MONGO_URL: {MONGO_URL}")
print(f"DB_NAME: {DB_NAME}")
print(f"COLLECTION_NAME: {COLLECTION_NAME}")

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
