# from flask import Flask
# from .Routers.TodoRouters import todo
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# # app.config.from_object('app.settings')
# app.register_blueprint(todo)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"