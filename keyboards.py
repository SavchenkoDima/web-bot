from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton
from models import models

beginning_kb = {
    'news': 'Последние новости',
    'products': 'Продукты',
    'sales': 'Продукты со скидкой',
    'about': 'информация о магазине',
}


product_kb = {
    'add to basket': 'Добавить в корзину',
    'show basket': 'Показать корзину'
}
basket_kb = {
    'delete': 'Удалить товар из корзины',
}

basket_buy_kb = {
    'Buy': 'Купить',
    'clear': 'очистить корзину'
}

hideBoard = ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard


class ReplyKB(ReplyKeyboardMarkup, ReplyKeyboardRemove):
    def __init__(self, resize_keyboard=True, one_time_keyboard=True, row_width=3):
        super().__init__(resize_keyboard=resize_keyboard,
                         one_time_keyboard=one_time_keyboard,
                         row_width=row_width)

    def generate_kb(self, *args):
        """
        :param args: button names
        :return:
        """
        buttons = [KeyboardButton(x) for x in args]
        self.add(*buttons)
        return self

    def hide_keyboard(self):
        hide = ReplyKeyboardRemove()
        return hide


class InlineKB(InlineKeyboardMarkup):

    queries = {
        'root': models.Category.get_root_categories()
    }

    def __init__(self, named_arg, lookup_fields='id', title_fields='title',  row_width=3, iterable=None, key=None):
        if all([iterable, key]):
           raise ValueError('Only one of fields: iterable, key can by set')
        super().__init__(row_width=row_width)
        self._iterable = iterable
        self._named_arg = named_arg
        self._lookup_fields = lookup_fields
        self._title_fields = title_fields
        self._query = self.queries.get(key)

    def generate_kb(self):
        buttons = []
        if not self._iterable:
            self._iterable = self._query
        for i in self._iterable:
            buttons.append(InlineKeyboardButton(
                text=getattr(i, self._title_fields),
                callback_data=f'{self._named_arg}_' + str(getattr(i, self._lookup_fields))
            ))
        self.add(*buttons)
        return self

    def generator_root_kb(self):
        if not self._iterable:
            self._iterable = models.Category.get_root_categories()
            return self.generate_kb()
        raise ValueError('iterable already set')
