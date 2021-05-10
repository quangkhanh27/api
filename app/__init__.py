from flask import Flask
from .Routers.TodoRouters import todo

app = Flask(__name__)
app.register_blueprint(todo)
