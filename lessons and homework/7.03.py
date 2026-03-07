class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.now = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.now > self.n:
            raise StopIteration
        result = self.now
        self.now += 2

        return result

# for x in EvenIterator(10):
#     print(x)


class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1  # начинаем с последнего элемента

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        result = self.data[self.index]
        self.index -= 1          # идём назад
        return result


# data = [10, 20, 30]
# for x in ReverseList(data):
#     print(x)

# ---------3----------
import numpy as np

arr = np.array([3, 7, 1, 9, 4])

# print(arr.max())
# print(arr.mean())

# -----------4---------
arr2 = np.array([2, 8, 4, 10, 3])
# print(arr2[arr2 > 5])

#-----------5----------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# print(a+b)

#----------6----------
arr3 = np.array([1, 2, 3, 4])

arr4 = arr3 * 3
print(arr4)





