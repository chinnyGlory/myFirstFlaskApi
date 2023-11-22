from mysql.connector import connect


def dbconnector():
    try:
        
        connector = connect(host = "localhost",user = "root", password = "",database ="schooldb",port = "3306" )
        cursor = connector.cursor(buffered = True,dictionary = True)
         
        return connector,cursor
    except Exception as z:
        print(str(z))