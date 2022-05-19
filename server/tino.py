from flask_restx import Resource,Api,Namespace
from flask import request
from secret import tino_dev_client_secret,tino_prod_client_secret
import requests
TINO = Namespace('tinoModule')

@TINO.route('/getToken')
class getToken(Resource):
    def post(self):
        data = request.json.get('data')
        code = data['code']
        client_id = data['clientId']
        redirect_uri = data['redirectUri']
        if data['env'] =='development':
            secret_key = tino_dev_client_secret
        else:
            secret_key = tino_prod_client_secret
            
        url = f"https://www.tistory.com/oauth/access_token?client_id={client_id}&client_secret={secret_key}&redirect_uri={redirect_uri}&code={code}&grant_type=authorization_code"
        r = requests.get(url)
        if r.status_code ==200:
            t = r.text.split('=')[-1]
            return {
                "access_token":t
            },200
        else:
            return{
                'msg':"request fail"
            },404
            
            
@TINO.route('/getInfo')
class getInfo(Resource):
    def post(self):
        data = request.json.get('data')
        access_token = data['accessToken']
        url = f"https://www.tistory.com/apis/blog/info?access_token={access_token}&output=json"
        r = requests.get(url)
        t = r.__dict__
        j = r.json()
        print(t)
        return{
            "2":j
        },200



        
@TINO.route('/contentpost')
class contentpost(Resource):
    def post(self):
        categories = {}
        data = request.json.get('data')
        access_token = data['accessToken']
        blog_name = data['blogName']
        title = data['title']
        content = data['content']
        visibility = data['visibility']
        category = data['category']
        published = data['published']
        slogan = data['slogan']
        tag = data['tag']
        accept_comment = data['acceptComment']
        password = data['password']
        url = "https://www.tistory.com/apis/category/list?"
        url += f"access_token={access_token}"
        url += "&output=json"
        url += f"&blogName={blog_name}"
        r = requests.get(url)
        if r.status_code == 200:
            j = r.json()
            if int(j['tistory']['status']) == 200:
                categories = {e["label"]:e['id'] for e in j['tistory']['item']['categories']}
                categories['']=0
            else:
                return {
                "msg":"Category request fail"
            },404
        else:
            return {
                "msg":"request fail"
            },404
        try:
            category = categories[category]
        except:
            category = 0
        params = {}
        url = "https://www.tistory.com/apis/post/write"
        params['access_token'] = access_token
        params['title'] = title
        params['output'] = 'json'
        params['blogName'] = blog_name
        params['content'] = content
        params['visibility'] = int(visibility)
        params['category'] = int(category)
        params['slogan'] = slogan
        print(",".join(tag))
        params['tag'] = ",".join(tag)
        params['slogan'] = slogan
        params['acceptComment'] = accept_comment
        params['password'] = password
      
  
        r = requests.post(url,data=params)
        if r.status_code == 200:
            j = r.json()
            return {
                'j':j
            },200
        else:{
            'j':r.text
        },404
 
 
 
 
 