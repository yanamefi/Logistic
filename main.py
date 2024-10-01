from fastapi import FastAPI, Depends
from user_actions.models import TruckDriverCreate, LogisticianCreate, BusinessOwnerCreate, Login
from user_actions.appLogic import register, accept_request, login
from user_actions.jwt_op import verify_token
from chat_actions.appLogic import create_chat, send_message, message_list
from chat_actions.models import Message

app = FastAPI()

objects = {"truck"}


@app.post("/user/register/truck")
async def user_reg(user: TruckDriverCreate):
    return register(user)


@app.post("/user/register/logistician")
async def logist_reg(user: LogisticianCreate):
    return register(user)


@app.post("/user/register/buisness")
async def buisness_reg(user: BusinessOwnerCreate):
    return register(user)


@app.post("/user/login")
async def login_user(user: Login):
    return login(user)


@app.get("/request/{request}")
async def req(request: str):
    return accept_request(request)


@app.post("/chat/create")
async def cr_chat(second_user: str, decoded_token: dict = Depends(verify_token)):
    return await create_chat([decoded_token["user_id"], second_user])


@app.post("/chat/{chat_id}/message")
async def transfer_message(message: Message, chat_id: str, decoded_token: dict = Depends(verify_token)):
    return send_message(message, chat_id, decoded_token)


@app.get("/chats/{chat_id}/messages/")
async def get_messages(chat_id: str):
    return await get_messages(chat_id)