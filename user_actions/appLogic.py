from settings import customer_db, redis_conn, site_directory
from user_actions.utils import send_email, hashing
from user_actions.jwt_op import jwt_en
import json


def register(credentials):
    if customer_db.find_one({"email": credentials.email}):
        return {"msg": "There is already an account with this email"}

    credentials.password = hashing(credentials.password)
    rand = hashing(credentials.email)
    credentials_dict = dict(credentials)
    del credentials_dict["password_confirmation"]
    credentials_json = json.dumps(credentials_dict)
    redis_conn.set(rand, credentials_json, ex=3600)

    send_email(f"{site_directory}/request/{rand}", credentials.email)
    return {"msg": "You successfully registered"}


def accept_request(request):
    mail = redis_conn.get(request)
    try:
        json_mail = json.loads(mail)
        user = customer_db.insert_one(json.loads(mail))
        redis_conn.delete(request)
        return {"msg": "account registrated",
                "cookie": jwt_en({"user_id": str(user["_id"]),
                                  "acc_ status": json_mail["acc_status"]}
                                 )}
    except TypeError:
        return {"msg": "code is not available anymore"}


def login(credentials):
    user = customer_db.find_one({"email": credentials.email})
    if user["password"] == hashing(credentials.password):
        return {"msg": "You logged in",
                "cookie": jwt_en({"user_id": str(user["_id"]),
                                  "acc_status": user["acc_status"]}
                                 )
                }
    else:
        return {"msg": "Wrong credentials"}
