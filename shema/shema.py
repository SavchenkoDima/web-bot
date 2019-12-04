from marshmallow import fields, Schema, validates, ValidationError


class PropertiesSchema(Schema):
    weight = fields.Float(min_value=0)


class TextsSchema(Schema):
    title = fields.String(unique=True)
    body = fields.String()


class LazyCatScheme(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    parent = fields.Nested('self')


class CategorySchema(Schema):
    id = fields.String()
    title = fields.String(required=True)
    description = fields.String()
    subcategory = fields.List(fields.Nested(LazyCatScheme), load_only=True)
    parent = fields.Nested('self', load_only=True)


class ProductSchema(Schema):
    id = fields.String()
    title = fields.String()
    description = fields.String()
    price = fields.Integer()
    new_prise = fields.Integer()
    is_discount = fields.Bool()
    properties = fields.Nested(PropertiesSchema)
    category = fields.Nested(CategorySchema, load_only=True, default=None)
    #photo_product = fields.String()


class UsersSchema(Schema):
    first_name = fields.String(required=True)
    username = fields.String(required=True)
    last_name = fields.String(required=True)
    user_id = fields.Integer(required=True)
    basket = fields.List(fields.Nested(ProductSchema))


class BasketSchema(Schema):
    user = fields.Nested(UsersSchema)
    basket_list = fields.List(fields.Nested(ProductSchema))
    bought = fields.Bool(default=False)
    bought_date = fields.DateTime()


class BasketHistorySchema(Schema):
    basket = fields.Nested(BasketSchema)