#!/usr/bin/python3
class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) != tuple or len(position) != 2\
                or type(position[0]) != int or type(position[1]) != int\
                or position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple \
of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return ((self.__size) ** 2)

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2\
                or type(value[0]) != int or type(value[1]) != int\
                or value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be a tuple \
of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(' ', end='')
            print("{}".format('#') * self.__size)
