from tasks.common import MyException


class ClassFather:
    _name = None
    registered_list = []

    @classmethod
    def register(cls):
        if cls != ClassFather and issubclass(cls, ClassFather):
            cls.registered_list.append(cls)
        else:
            raise MyException

    @classmethod
    def get_name(cls):
        if cls in cls.registered_list:
            return cls._name
        else:
            raise MyException


class User1(ClassFather):
    _name = 'name_user1'


class User2(ClassFather):
    _name = 'name_user2'
