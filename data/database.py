import motor.motor_asyncio
from config import MONGODB_URI

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client.ecoquest

async def get_user_state(user_id: int):
    # Retrieve user state from the database
    user = await db.users.find_one({"user_id": user_id})
    return user["state"] if user else None

async def update_user_state(user_id: int, new_state: dict):
    # Update or insert user state in the database
    await db.users.update_one(
        {"user_id": user_id},
        {"$set": {"state": new_state}},
        upsert=True
    )
