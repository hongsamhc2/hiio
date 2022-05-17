from flask_restx import Resource,Api,Namespace
from flask import request
import jwt
JWTSCPACE = Namespace('jwtmodule')
SCRET = "asjwc0skcmm20cmnz,snc-djnwncjcnxocnw02c"

@JWTSCPACE.route('/encode')
class JWTEncode(Resource):
    def post(self):
        data = request.json.get('data')
        encoded = jwt.encode(data,SCRET,algorithm="HS256")
        return {
            'token':encoded
        }
        
@JWTSCPACE.route('/decode')
class JWTDecode(Resource):
    def post(self):
        data = request.json.get('data')
        decoded = jwt.decode(data,SCRET,algorithms=["HS256"])
        return decoded