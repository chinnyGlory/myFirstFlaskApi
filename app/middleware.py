from flask import request,abort

def checkuser(func):
    def wrapper(*args,**kwargs):
        print('middleware was mentioned')
        token = request.args.get('token')
        
        
        if not (token == "admin"):
            abort(403)
        else:
        
          return func(*args,**kwargs)
      
    return wrapper
    
    