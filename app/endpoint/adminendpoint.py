from flask import Blueprint,request
from..schoolapp.admin import view_users,select_user,pick_user,picks
from..middleware import checkuser

admin = Blueprint('admin',__name__)

@admin.get('/')
@checkuser
def view():
    feedback = view_users()
    return feedback


@admin.get('/select')
def select():
    data = request.json
    feedback = select_user(data['age'])
    return feedback

@admin.get('/set')
def pick():
    
   data = request.json
   feedback = pick_user(data['age'])
   return feedback

@admin.get('/chose')
def picker():
    
   data = request.json
   feedback = picks(data)
   return feedback