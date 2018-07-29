from flask_restful import Resource

class Requests(Resource):
	def get(self):
		return {"message": "Hello, World!"}