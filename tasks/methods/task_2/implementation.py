from tasks.common import MyException


class ClassFather:
    _name = None
    registered_list = []

    def get_name(self):
        if self._name is None or self not in self.registered_list:
            raise MyException
        else:
            return self._name

    def register(self):
        if self._name is None:
            raise MyException
        self.registered_list.append(self)


class User1(ClassFather):
    _name = 'name_user1'


class User2(ClassFather):
    _name = 'name_user2'
