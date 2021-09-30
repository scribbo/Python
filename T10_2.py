from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.n = name
        self.s = None

    @property
    def name(self):
        return self.n

    @abstractmethod
    def get_s(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 30:
            self.__v = 30
        elif v > 62:
            self.__v = 62
        else:
            self.__v = v

    def get_s(self):
        self.s = (self.__v / 6.5) + 0.5
        return self.s


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 120:
            self.__h = 120
        elif h > 220:
            self.__h = 220
        else:
            self.__h = h

    def get_s(self):
        self.s = (2 * self.__h) + 0.3
        return self.s


class Collection:
    def __init__(self):
        self.my_list = []
        self.s = 0

    def add_clothes(self, my_clothes: Clothes):
        self.my_list.append(my_clothes)
        self.s += my_clothes.get_s()

    def __str__(self):
        my_string = ''
        for el in self.my_list:
            my_string += 'Площадь ткани для ' + el.name + ' равна ' + str(round(el.get_s(), 2)) + '\n'
        my_string = my_string + 'Суммарная площадь ткани для всей коллекции равна ' + str(round(self.s, 2))
        return my_string


m_list = Collection()
m_list.add_clothes(Coat('green coat', 46))
m_list.add_clothes(Suit('striped suit', 182))
print(m_list)
