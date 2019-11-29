from flask_restful import Api
from flask import Flask
from resousers.resource import CategoryResurse, ProductResurse
import config

app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryResurse, '/Category/', '/Category/<string:id>')
api.add_resource(ProductResurse, '/Product/', '/Product/<string:id>')

if __name__ == '__main__':
    app.run(debug=True, port=config.HOST_PORT)

