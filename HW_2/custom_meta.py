class CustomMeta(type):

    def __new__(cls, name, bases, dct):

        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        custom_attr = dict(('custom_' + name, value) for name, value in attrs)

        return super(CustomMeta, cls).__new__(cls, name, bases, custom_attr)


class CustomClass(metaclass=CustomMeta):
    x = 50

    @staticmethod
    def line():
        return 100


inst = CustomClass()
inst.custom_x
inst.custom_line()

# inst.x  # ошибка
# inst.line() # ошибка
