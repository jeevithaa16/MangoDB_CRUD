from flask import Flask,Blueprint
from flask_cors import CORS
from crud_app.points import routes

def create_app():
    web_app = Flask(__name__)
    CORS(web_app)

    api_blueprint = Blueprint('api_blueprints',__name__)
    api_blueprint = routes(api_blueprint)
    web_app.register_blueprint(api_blueprint,url_prefix='/')
    return web_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)