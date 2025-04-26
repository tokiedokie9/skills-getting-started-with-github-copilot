from motor.motor_asyncio import AsyncIOMotorClient
from typing import Dict, Any

# MongoDB connection
client = AsyncIOMotorClient('mongodb://localhost:27017')
db = client.mergington_high
activities_collection = db.activities

async def init_db():
    # Drop existing collection to start fresh
    await activities_collection.drop()
    
    # Initial activities data
    initial_activities = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Join the school soccer team and compete in matches",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
            "max_participants": 22,
            "participants": ["liam@mergington.edu", "noah@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Practice and compete in basketball tournaments",
            "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["ava@mergington.edu", "mia@mergington.edu"]
        },
        "Art Club": {
            "description": "Explore various art techniques and create projects",
            "schedule": "Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
        },
        "Drama Club": {
            "description": "Participate in plays and improve acting skills",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 20,
            "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
        },
        "Math Club": {
            "description": "Solve challenging math problems and prepare for competitions",
            "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
            "max_participants": 10,
            "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
        },
        "Science Club": {
            "description": "Conduct experiments and explore scientific concepts",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["elijah@mergington.edu", "lucas@mergington.edu"]
        }
    }
    
    # Insert activities into MongoDB
    for name, details in initial_activities.items():
        await activities_collection.insert_one({
            "_id": name,  # Use activity name as the document ID
            **details
        })

async def get_all_activities() -> Dict[str, Any]:
    """Get all activities from the database"""
    cursor = activities_collection.find()
    activities = {}
    async for doc in cursor:
        name = doc.pop('_id')  # Remove _id and use it as the key
        activities[name] = doc
    return activities

async def get_activity(name: str) -> Dict[str, Any]:
    """Get a specific activity by name"""
    return await activities_collection.find_one({"_id": name})

async def update_activity_participants(name: str, participants: list):
    """Update the participants list for an activity"""
    await activities_collection.update_one(
        {"_id": name},
        {"$set": {"participants": participants}}
    )