from chat_actions.models import Chat
from settings import chat_db, customer_db, messages_db, site_directory
from typing import List
from bson import ObjectId
from datetime import datetime


async def create_chat(participants: List[str]):
    chat = chat_db.chats.find_one({"participants": {"$all": participants}})

    if chat:
        return str(chat['_id'])

    second_user = customer_db.find_one({"_id": ObjectId(participants[1])})

    if second_user is None:
        return {"msg": "User not found"}

    new_chat = Chat(participants=participants)
    result = chat_db.chats.insert_one(new_chat.__dict__)

    return {"chat_id": str(result.inserted_id),
            "link": f"{site_directory}/chat/{str(result.inserted_id)}"}


def send_message(message, chat_id, user):
    message_data = message.__dict__
    message_data['timestamp'] = datetime.now()
    message_data['chat_id'] = chat_id
    message_data['sender_id'] = user["user_id"]
    result = messages_db.insert_one(message_data)

    # Update last_message in chat
    messages_db.chats.update_one(
        {"_id": ObjectId(message_data["chat_id"])},
        {
            "$set": {
                "last_message": str(result.inserted_id),
                "updated_at": datetime.now()
            }
        }
    )

    return {"message_id": str(result.inserted_id)}


def message_list(chat_id):
    messages = chat_db.messages.find({"chat_id": chat_id})
    return [msg for msg in messages]
