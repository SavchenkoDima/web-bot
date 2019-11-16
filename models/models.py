from mongoengine import *
import datetime
import time

connect('web_shop_bot')


class Texts(Document):
    title = StringField(unique=True)
    body = StringField(max_length=4096)
    photo_product = ImageField()


class Properties(DynamicEmbeddedDocument):
    weight = FloatField(min_value=0)
    pass


class Category(Document):
    title = StringField(max_length=255, required=True)
    description = StringField(max_length=512)
    subcategory = ListField(ReferenceField('self'))
    parent = ReferenceField('self')

    @property
    def is_parent(self):
        return bool(self.subcategory)

    @property
    def is_root(self):
        return not bool(self.parent)

    @property
    def get_product(self, **kwargs):
        return Product.objects(category=self, **kwargs)

    def add_subcategory(self, obj):
        obj.parent = self
        obj.save()
        self.subcategory.append(obj)
        self.save()

    @classmethod
    def get_root_categories(cls):
        return cls.objects(parent=None)


class Product(Document):
    title = StringField(max_length=255)
    description = StringField(max_length=1024)
    price = IntField(min_value=0)
    new_prise = IntField(min_value=0)
    is_discount = BooleanField(default=False)
    properties = EmbeddedDocumentField(Properties)
    category = ReferenceField(Category)
    photo_product = ImageField()

    @property
    def get_price(self):
        if self.is_discount:
            return str(self.new_prise / 100)
        return str(self.price / 100)

    @classmethod
    def get_discount_products(cls, **kwargs):
        return cls.objects(is_discount=True)


class Users(Document):
    first_name = StringField(max_length=255, required=True)
    username = StringField(max_length=255, required=True)
    last_name = StringField(max_length=255, required=True)
    user_id = IntField(required=True)
    basket = ListField(ReferenceField(Product))

    def add_product(self, obj):
        """
        :type obj: object
        """
        self.basket.append(obj)

    def count_product(self):
        return len(self.basket)


class Basket(Document):
    user = ReferenceField(Users)
    basket_list = ListField(ReferenceField(Product))
    bought = BooleanField(default=False)
    bought_date = DateTimeField()

    @property
    def basket_closed(self):
        self.bought = True
        self.bought_date = datetime.datetime.now()
        self.save()


class BasketHistory(Document):
    basket = ReferenceField(Basket)
