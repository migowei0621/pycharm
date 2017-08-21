import numpy as np

class DynamicArray(object):
    def __init__(self, item_type):
        self.__data = np.zeros(10, item_type)
        self.__size = 0

    def get_data(self):
        return self.__data[:self.__size]

    def append(self, value):
        if len(self.__data) == self.__size:
            self.__data = np.resize(self.__data, int(len(self.__data))* 1.25)

        self.__data[self.__size] = value
        self.__size += 1


item_type = np.dtype({
    "names":["id", "x", "y", "z"],
    "formats":["i4", "f8", "f8", "f8"]
})

da = DynamicArray(item_type)

for i in range(100):
    da.append((i, i*0.1,  i*0.2, i*0.3))

data = da.get_data()
print(data)