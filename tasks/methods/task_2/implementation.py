from tasks.common import MyException


class ClassFather:
    registered_list = []

    def get_name(self):
        if self in self.registered_list:
            return self._name
        else:
            raise MyException

    def register(self):
        if isinstance(self, (User1, User2)):
            self.registered_list.append(self)
        else:
            raise MyException


class User1(ClassFather):
    _name = 'name_user1'


class User2(ClassFather):
    _name = 'name_user2'
