from flask import Blueprint,request
from..schoolapp.user import create_data,create_user

user = Blueprint('user',__name__)

@user.get('/insert')
def insert():
    data = request.json
    feedback = create_user(data)
    return feedback
    