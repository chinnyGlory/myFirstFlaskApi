from.import dbconnector

def create_user(data):
    
    if not data: return {"message":"user not found"}
    try:
        
        
    
        db = dbconnector()
    
        if not db : return
        connector,cursor = db
    
        sql = f"""INSERT INTO `student`(`fullname`, `class`, `age`, `guardian_name`, `guardian_no`, `address`) VALUES ('{data['fullname']}','{data['class']}','{data['age']}','{data['guardian_name']}','{data['guardian_no']}','{data['address']}')
        """
   
        cursor.execute(sql)
        connector.commit()
        connector.close()
        return {"message":"student data is created"}
    except Exception as c:
        return(str(c))
        



def create_data(data):
    
    if not data: return {"message":"user not found"}
    
    db = dbconnector()
    
    if not db : return
    connector,cursor = db
    sql = f"""INSERT INTO `teacher`(`phone`,`fullname`,`address` ,`class`, `subject`) VALUES ('{data['phone']}','{data['fullname']}','{data['address']}','{data['class']}','{data['subject']}'"""
    cursor.execute(sql)
    connector.commit()
    connector.close()
    return {"message":"teacher's data is created"}
