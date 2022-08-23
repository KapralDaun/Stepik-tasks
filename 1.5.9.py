class Cart:
    goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        list = []
        for i in self.goods:
            strok = i.name + ': ' + str(i.price)
            list.append(strok)
        return list


class Table:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:

    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
tv1 = TV("Samsung", 22800)
tv2 = TV("LG", 14880)
table = Table("IKEA", 20000)
N1 = Notebook("Acer", 30000)
N2 = Notebook("Asus", 40000)
cup = Cup("Cup", 1000)
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(N1)
cart.add(N2)
cart.add(cup)
print(cart.get_list())