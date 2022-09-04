from flask_pymongo import pymongo
from flask import request

client = pymongo.MongoClient("mongodb+srv://jeevithaa16:jeevithaa16@cluster0.l9uytaf.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('testdb')
collection = pymongo.collection.Collection(db,'testcol')
print("MongoDB connected successfully")

def routes(endpoints):

    @endpoints.route('/hello', methods=['GET'])
    def hello():
        resp = "Hello world"
        print(resp)
        return resp

    @endpoints.route('/create_user', methods=['POST'])
    def create_user():
        resp = {}
        try:
            req_body = request.json
            collection.insert_one(req_body)
            print("User added.")
            status = {
                "code":"200",
                "message":"User added to database."
            }
        except Exception as e:
            print(e)
            status = {
                "code":"500",
                "message":str(e)
            }
        resp["status"] = status
        return resp

    @endpoints.route('/get_user', methods=['GET'])
    def get_user():
        resp = {}
        try:
            id = int(request.args.get('id'))
            user = collection.find_one({"id":id})
            print(user)
            status = {
                "code":"200",
                "message":"User found"
            }
        except Exception as e:
            print(e)
            status = {
                "code":"500",
                "message":str(e)
            }
        resp["user"] = {
            "id":user['id'],
            "name":user['name'],
            "mail_id":user['mail_id']
        }
        resp["status"] = status
        return resp

    @endpoints.route('/update_user', methods=['PUT'])
    def update_user():
        resp = {}
        try:
            req_body = request.json
            collection.update_one({
                "id":req_body['id']
            },{
                "$set":req_body['updated_data']
            })
            print("User updated.")
            status = {
                "code":"200",
                "message":"User updated in database."
            }
        except Exception as e:
            print(e)
            status = {
                "code":"500",
                "message":str(e)
            }
        resp["status"] = status
        return resp

    @endpoints.route('/delete_user', methods=['DELETE'])
    def delete_user():
        resp = {}
        try:
            id = int(request.args.get('id'))
            collection.delete_one({"id":id})
            print("User deleted.")
            status = {
                "code":"200",
                "message":"User deleted from database."
            }
        except Exception as e:
            print(e)
            status = {
                "code":"500",
                "message":str(e)
            }
        resp["status"] = status
        return resp


    return endpoints