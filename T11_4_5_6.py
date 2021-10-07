from abc import ABC, abstractmethod


class Hardware(ABC):
    def __init__(self, name, port):
        self.name = name
        self.port = port

    @abstractmethod
    def __str__(self):
        pass


class Printer(Hardware):
    def __init__(self, name, port, color):
        super().__init__(name, port)
        self.color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, bool):
        if bool in ['True', 'true', 'Yes', 'yes', 'y', 'Y', 'да', 'Да', '+', 'color', 'Color', True]:
            self.__color = True
        else:
            self.__color = False

    def __str__(self):
        if self.__color:
            return 'Color printer ' + str(self.name) + ' on a tcp port ' + str(self.port)
        else:
            return 'Black&White printer ' + str(self.name) + ' on a tcp port ' + str(self.port)


class Monitor(Hardware):
    def __init__(self, name, port, w, h):
        super().__init__(name, port)
        self.resolution = str(w) + 'x' + str(h)

    def __str__(self):
        return 'Monitor ' + str(self.name) + ' on a ' + str(self.port) + ' port ' + self.resolution


class Scanner(Hardware):
    def __init__(self, name, port):
        super().__init__(name, port)

    def __str__(self):
        return 'Scanner ' + str(self.name) + ' on a ' + str(self.port) + ' port'


class Warehouse:
    def __init__(self):
        self.hw_list = []
        self.count = 0

    def get_count(self):
        return self.count

    def add_hardware(self, my_hardware: Hardware, qtty):
        try:
            for i in range(qtty):
                self.hw_list.append(my_hardware)
            self.count += qtty
        except TypeError:
            print('Quantity shall be an integer number')

    def move(self, other, ordnum):
        if len(self.hw_list) >= ordnum:
            other.add_hardware(self.hw_list[ordnum], 1)
            print(f'{self.hw_list[ordnum]} is moved successfully')
            del self.hw_list[ordnum]
            self.count -= 1
        else:
            print('Hardware index is out of range')

    def __str__(self):
        my_string = ''
        for el in self.hw_list:
            my_string += str(el) + '\n'
        my_string = my_string + 'Total amount of hardware on central warehouse: ' + str(self.count)
        return my_string


central_wh = Warehouse()
central_wh.add_hardware(Printer('LSB-20', 'usb', 'Да'), 'two')
central_wh.add_hardware(Monitor('Viewsonic', 'pci-e', 640, 480), 5)
central_wh.add_hardware(Scanner('HP', 'usb'), 3)
IT = Warehouse()
Accounting = Warehouse()

central_wh.move(IT, 4)
central_wh.move(Accounting, 9)

print('IT:')
print(IT)
print('Accounting:')
print(Accounting)
print('Whs:')
print(central_wh)