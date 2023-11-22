from . import dbconnector


def create_admin():
    db = dbconnector()

    if not db : return
    connector,cursor = db

    
    try:
        
        
        sql = f'''INSERT INTO admin('email','fullname','address') VALUES('chinnny@gmail.com','ada','no7 tddygty')'''
        cursor.execute(sql)
        connector.commit()
        connector.close()
        print('default admin created')
        
    except Exception as e:
        print ('email already exist')
        
        
def view_users():
    db = dbconnector()
    if not db : return
    connector,cursor = db
    sql = """ SELECT * FROM student"""
    cursor.execute(sql)
    all_user = cursor.fetchall()
    connector.close()
    
    if not all_user : return {'message':'no user found'}
    
    return{'message':'user found',
           'message': all_user}

def select_user(age):
    db = dbconnector()
    if not db : return
    connector,cursor = db
    sql = """ SELECT * FROM student"""
    cursor.execute(sql)
    all_user = cursor.fetchall()
    connector.close()
    
    if not all_user : return {'message':'no user found'}
    
    selectedUsers = [user for user in all_user if user.get('age',0) < age]
    
    if not selectedUsers : return {'message': "no user under the age group"}
    
    return{'message':'user found',
           'message': selectedUsers} 
    
    
    
def pick_user(age)    :
    db = dbconnector()
    if not db :return
    connector,cursor = db
    sql = """ SELECT* FROM student"""
    cursor.execute(sql)
    many_user = cursor.fetchall()
    connector.close()
    if not many_user : return{'message':'no user found'}
    selecteduser = [user for user in many_user if user.get('age',0) > age]
    if not selecteduser : return{'message':'no user found'}
    return {'message':'user found',
            'message': selecteduser}
    


def picks(data)    :
    db = dbconnector()
    if not db :return
    connector,cursor = db
    try:
        sql = f""" SELECT * FROM student WHERE `class`= '{data['class']}' """
        cursor.execute(sql)
        many_user = cursor.fetchall()
        connector.close()
        
        if not many_user : return {'message':' no user found'}
        
        return {'message':'user found',
            'data': many_user}
    
    except Exception as e:
        return f"error:  {e}"
        
    
   
    
        
def view():
    db = dbconnector()
    if not db : return
    connector,cursor = db
    sql = """ SELECT * FROM teacher"""
    cursor.execute(sql)
    allteachers = cursor.fetchall()
    connector.close()
    
    if not allteachers : return {'message':'no user found'}
    
    return{'message':'user found',
           'message': all}
        

