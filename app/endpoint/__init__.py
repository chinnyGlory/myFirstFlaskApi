from flask import Blueprint
from.adminendpoint import admin
from.userendpoint import user


Api = Blueprint("Api",__name__)

Api.register_blueprint(user,url_prefix = '/user')
Api.register_blueprint(admin,url_prefix = '/admin')