from flask import Flask,request,make_response
from flask_cors import CORS
from flask_restx import Api, Resource
from oauthJWT import JWTSCPACE
app = Flask(__name__,static_url_path='/static')
api = Api(app)
CORS(app)

api.add_namespace(JWTSCPACE,'/jwt')


@app.before_request
def before_first_request():
    registered_url = ['http://localhost:8080',"https://hiio420.com"]
    origin_url = request.origin
    if request.method !='OPTIONS' :
        access_token = request.headers.get("Authorization")
        fail_resp = make_response("Authorization denied", 400)
        if access_token != 'alkcn122123qalkn3jnvjel34tj79g3sajsnck678' and 'api' in request.endpoint :
            return fail_resp
    if origin_url not in registered_url:
        fail_resp = make_response("URL is not registered", 400)
        return fail_resp


if __name__ == "__main__":
    app.run(debug=True,port=48952)