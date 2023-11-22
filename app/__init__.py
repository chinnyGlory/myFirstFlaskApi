from flask import Flask
from.migrate import migration
from.endpoint import Api

def creation():
    
    app = Flask(__name__)
    migration()
    app.register_blueprint(Api,url_prefix ="/Api/v4")
    
    

    
    return app