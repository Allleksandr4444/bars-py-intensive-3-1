from tasks.common import MyException


class ClassFather:
    _name = None
    registered_list = []

    def get_name(self):
        if self.__class__ in self.registered_list:
            return self._name
        else:
            raise MyException

    def register(self):
        if self.__class__ == ClassFather:
            raise MyException
        self.registered_list.append(self.__class__)


class User1(ClassFather):
    _name = 'name_user1'


class User2(ClassFather):
    _name = 'name_user2'
