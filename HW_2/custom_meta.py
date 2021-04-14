class CustomMeta(type):

    def __new__(cls, name, bases, dct):
        custom_attr = (
            (name, value) for name, value in dct.items()
            if not (name.startswith('__') and name.endswith('__'))
        )
        all_attr = dict(('custom_' + name, value) for name, value in custom_attr)
        magic_attrs = dict((name, value) for name, value in dct.items() if (name.startswith('__') and name.endswith('__')))
        all_attr = all_attr | magic_attrs
        return super().__new__(cls, name, bases, all_attr)

    def __init__(cls, name, bases, dct):
        print(dct)
        super().__init__(name, bases, dct)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self):
        self.y = 300

    def __str__(self):
        return 'test_string'

    @staticmethod
    def __private_method():
        return 0

    @staticmethod
    def line():
        return 100
