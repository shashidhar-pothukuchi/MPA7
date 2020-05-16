from flask import Flask
from flask_restful import Api, Resource, reqparse
# import scrap
import run
import mine
import search
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
api = Api(app)

class Search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("pname")
        args = parser.parse_args()
        data = search.searchname(args['pname'])
        return data,200

class Crawl(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("pid")
        args = parser.parse_args()
        data=run.getreviews(args['pid'])
        return data, 200

class Analyse(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("pid")
        args = parser.parse_args()
        data=mine.startMine(args['pid'])
        return data, 200

api.add_resource(Search,"/search")
api.add_resource(Crawl, "/scrap")
api.add_resource(Analyse, "/analyse")
app.run( host = '0.0.0.0',port = '5000', debug=True)
