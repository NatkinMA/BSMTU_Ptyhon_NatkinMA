import ctypes
import sys


class MyList:
    def __init__(self):
        self.length = 0
        self.capacity = 8
        self.array = (self.capacity * ctypes.py_object)()

    def append(self, item):
        if self.length == self.capacity:
            self._resize(self.capacity*2)
        self.array[self.length] = item
        self.length += 1

    def pop(self):
        self.length -= 1
        if self.length <= (self.capacity // 2 + 1):
            self._resize(self.capacity // 2 + 1)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.array[index]

    def _resize(self, new_capacity):
        new_array = (new_capacity * ctypes.py_object)()
        for index in range(self.length):
            new_array[index] = self.array[index]
        self.array = new_array
        self.capacity = new_capacity

list = MyList()
list.append("один")
list.append("два")

print(f"Размер списка из {len(list)} элементов: ", sys.getsizeof(list), "байт.")

print("Добавляем элементы в массив:")
for i in range(20):
    list.append(i)
    print(f"Размер списка из {len(list)} элементов: ", sys.getsizeof(list), "байт.")
    #print(list[i])

print("Удаляем элементы из массива:")
for i in range(20):
    list.pop()
    print(f"Размер списка из {len(list)} элементов: ", sys.getsizeof(list), "байт.")
