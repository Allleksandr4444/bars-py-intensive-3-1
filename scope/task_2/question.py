"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

"""
При выполнения кода будет выведено:

Test message
None

Внутри функции transmit_to_space() мы задаём вложенную функцию data_transmitter(). Далее уже вызывается сама функция 
data_transmitter(). При вызове функции data_transmitter необходимо напечатать переменную message.
Внутри функции data_transmitter() переменная message не задана. Поэтому переменная message будет искаться на уровень
выше по правилам LEGB. И найдется в функции transmit_to_space(). После на экран будет выведено значение переменной
message.
После будет выведено None, т.к. сама в самой функции transmit_to_space() отсутствует return. Тем самым 
функция transmit_to_space() ничего не возвращает.
"""