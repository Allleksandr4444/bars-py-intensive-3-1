class Tuple:
    """
    Создает неизменяемый объект с упорядоченной структурой и методами count и index.
    При создании принимается последовательность объектов.
    """

    def __init__(self, *args):
        self.__arguments = args


    def __getitem__(self, item):
        return self.__arguments[item]

    def count(self, value) -> int:
        """
        Возвращает количество появлений value в объекте.
        Args:
            value: количество вхождений в объекте
        """
        sum_count = 0
        for i in range(len(self.__arguments)):
            if self.__arguments[i] == value:
                sum_count += 1
        return sum_count

    def index(self, value) -> int:
        """
        Возвращает индекс первого вхождения элемента в объекте.
        Args:
            value: индекс искомого элемента
        """
        if value not in self.__arguments:
            raise ValueError

        for i in range(len(self.__arguments)):
            if value == self.__arguments[i]:
                return i
