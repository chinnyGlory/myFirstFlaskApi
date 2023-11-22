from . import dbconnector
def create_Admintable():
    db = dbconnector()
    if not db : return
    connector,cursor = db
    sql = """ CREATE TABLE IF NOT EXISTS admin(
       id INT(2) PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(100) UNIQUE NOT NULL,
       fullname TEXT(18) NOT NULL,
       address VARCHAR(100) NOT NULL
        )"""
    cursor.execute(sql)
    connector.commit()
    connector.close()
    print ("admintable created")
    
def create_tutortable():
    db = dbconnector()
    if not db : return
    connector,cursor = db
    sql = """ CREATE TABLE IF NOT EXISTS teacher(
       id INT(2) PRIMARY KEY AUTO_INCREMENT,
       phone INT(14) UNIQUE NOT NULL,
       fullname VARCHAR(18)NOT NULL,
       address VARCHAR(100)NOT NULL,
       class VARCHAR(10)NOT NULL,
       subject TEXT(20) NOT NULL)"""
    cursor.execute(sql)
    connector.commit()
    connector.close()
    print("teachers table created")
    
def create_studentable():
    
        
    db = dbconnector()
    if not db: return
    
    connector,cursor = db
    
    sql = """ CREATE TABLE IF NOT EXISTS student(

        id INT(2) PRIMARY KEY AUTO_INCREMENT,
        fullname TEXT(25)NOT NULL,
        class VARCHAR(10) NOT NULL,
        age  INT(3) NOT NULL,
        guardian_name TEXT(15) UNIQUE NOT NULL,
        guardian_no INT(14) NOT NULL,
        address VARCHAR(100) NOT NULL)"""
    cursor.execute(sql)
    connector.commit()
    connector.close()
    print('student table created')
    
       
       

    