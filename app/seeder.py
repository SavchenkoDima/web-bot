from mongoengine import connect
import models.models

from models.models import *

# connect('web_shop_bot')

# for i in range(5):
#     obj = models.models.Category(**{'title': f'root {i}',
#                              'description': f'deck {i}'}).save()
#     obj.add_subcategory(models.models.Category(**{'title': f'root {i}',
#                              'description': f'deck {i}'}))
#
# object = models.models.Category.objects(parent__ne=None)
#
# for i in object:
#     print(i.parent)
#     i.add_subcategory(models.models.Category(**{'title': f'sub-sub {i}', 'description': f'd {i}'}))

# product = Product.objects()

# for i in product:
#     print(i.id)
#     category_obj_db = Product.objects.get(id=i.id)
#     with open('imag.jpg', 'rb') as f:
#         category_obj_db.photo_product.put(f, collection_name='images/jpeg')
#         category_obj_db.save()



# product_dict = {
#     'title': 'SAMSUNG WW60J30G03WDUA',
#     'description': 'Габариты (ВхШхГ): 85x60x45 см',
#     'price': 11499,
#     'new_prise': 0,
#     'is_discount': False,
#     #'properties': True,
#     'category': category_obj_db
# }

"""
Заливка котегорий подкатегорий и под-под категорий.
"""
main_cat = ('computers-notebooks', 'appliances', 'Instruments')

a = {'computers-notebooks': ('Notebooks', 'Tablets', 'Accessories'),
     'appliances': ('Refrigerators', 'Washingmachines', 'Cooker'),
     'Instruments': ('Tool', 'Equipment', 'Handtool')
     }
b = dict(Notebooks=('Asus', 'Acer', 'HP'),
         Tablets=('8"', '10"', '11"'),
         Accessories=('headphones', 'Memory-cards', 'Cleaning-products'),
         Refrigerators=('Single-chamber', 'Bicameral', 'Side-by-side'),
         Washingmachines=('Narrow', 'With drying', 'With steam'),
         Cooker=('Gas', 'Electric', 'on coal'),
         Tool=('screwdriver', 'cutting machine', 'drill'),
         Equipment=('chainsaw', 'generator', 'compressor'),
         Handtool=('screwdriver', 'hammer', 'knife'),
         )

for i in main_cat:
    print('i=', i)
    category_dict = {
        'title': i,
        'description': f'about {i}',
        # 'subcategory': ,
        # 'parent'
    }
    new_cat = Category(**category_dict).save()

    for value in a.get(i):
        print('value=', value)
        main = Category.objects.get(title=i)
        category_dict = {
            'title': value,
            'description': f'about {value}',
        }
        main.add_subcategory(Category(**category_dict))

        for val in b.get(value):
            print('val', val)
            main = Category.objects.get(title=value)
            category_dict = {
                'title': val,
                'description': f'about {val}',
            }
            main.add_subcategory(Category(**category_dict))

# category_obj_db = Category.objects.get(title='screwdriver')
#
# product_dict = {
#     'title': 'screwdriver',
#     'description': 'screwdriver',
#     'price': 10000,
#     'new_prise': 0,
#     'is_discount': False,
#     'category': category_obj_db
# }
# new_pro = Product(**product_dict).save()

# for i in range(3):
#     main = Category.objects.get(title=main_cat[0])
#     category_dict = {
#         'title': middle_cat_com[i],
#         'description': f'about {middle_cat_com[i]}',
#     }
#     main.add_subcategory(Category(**category_dict))

    # new_cat = Category(**category_dict)
    # new_cat.save()

# product = Product.objects.get(id='5dc7130ee5712505491e96bd')
# user_obj = Users.objects.get(id='5dc7df24850aabc50a9dd346')
#
# user_obj.add_product(product)
# user_obj.save()
