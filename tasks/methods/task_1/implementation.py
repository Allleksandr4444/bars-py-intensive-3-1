class Coffee:
    def __init__(self, *args):
        self.ingridients = args

    def __repr__(self):
        return f'Кофе с игридиентами : {self.ingridients}'

    @classmethod
    def cappuccino(cls):
        return cls(['milk', 'espresso'])

    @classmethod
    def latte(cls):
        return cls(['milk', 'espresso', 'foam'])

    @classmethod
    def glace(cls):
        return cls(['coffee', 'ice cream', 'chocolate'])
