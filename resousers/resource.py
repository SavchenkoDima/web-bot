
from flask_restful import Resource
from flask import request, jsonify
from models.models import *
from shema.shema import *


class UserResurse(Resource):

    def get(self, id=None):
        if not id:
            objects = Users.objects
            return UsersSchema().dump(objects, many=True)
        return UsersSchema().dump(Users.objects(id=id).get())

    def post(self):
        error = UsersSchema().validate(request.json)
        if error:
            return error
        obj = Users(**request.json).save()
        return UsersSchema().dump(Users.objects(id=obj.id).get())

    def put(self, id):
        obj = Users.objects(id=id).get()
        obj.update(**request.json)
        return UsersSchema().dump(obj.reload())

    def delete(self, id):
        obj = Users.objects(id=id).delete()
        if obj == 1:
            return jsonify(**{'delete': 'ok'})
        else:
            return jsonify(**{'delete': 'Error'})


class ProductResurse(Resource):

    def get(self, id=None):
        # print(request.headers)
        # re = dict(request.headers)
        # print(re['Key'])

        if not id:
            objects = Product.objects
            return ProductSchema().dump(objects, many=True)
        return ProductSchema().dump(Product.objects(id=id).get())

    def post(self):
        print(request)
        error = ProductSchema().validate(request.json)
        if error:
            return error
        obj = Product(**request.json).save()
        return ProductSchema().dump(Product.objects(id=obj.id).get())

    def put(self, id):
        obj = Product.objects(id=id).get()
        obj.update(**request.json)
        return ProductSchema().dump(obj.reload())

    def delete(self, id):
        obj = Product.objects(id=id).delete()
        if obj == 1:
            return jsonify(**{'delete': 'ok'})
        else:
            return jsonify(**{'delete': 'Error'})


class CategoryResurse(Resource):

    def get(self, id=None):
        if not id:
            objects = Category.objects
            return CategorySchema().dump(objects, many=True)
        return CategorySchema().dump(Category.objects(id=id).get())

    def post(self):
        error = CategorySchema().validate(request.json)
        if error:
            return error
        obj = Category(**request.json).save()
        return CategorySchema().dump(Category.objects(id=obj.id).get())

    def put(self, id):
        obj = Category.objects(id=id).get()
        obj.update(**request.json)
        return CategorySchema().dump(obj.reload())

    def delete(self, id):
        obj = Category.objects(id=id).delete()
        if obj == 1:
            return jsonify(**{'delete': 'ok'})
        else:
            return jsonify(**{'delete': 'Error'})