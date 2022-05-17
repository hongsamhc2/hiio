from flask import Flask
from flask_cors import CORS
import flask_cors
from flask_restx import Api, Resource
from oauthJWT import JWTSCPACE
app = Flask(__name__,static_url_path='/static')
api = Api(app)
CORS(app)

api.add_namespace(JWTSCPACE,'/jwt')

if __name__ == "__main__":
    app.run(debug=True,port=48952)