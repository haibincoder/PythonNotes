def bubble_sort(array):
    length = len(array)
    for i in range(0,length):
        for j in range(i, length - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

array = [2, 4, 6, 2, 0, 63, 12, 56, 45, 6, 34, 6, 32, 23, 54, 4]
print(array)
bubble_sort(array)
print(array)

# if __name__ = '__main__':
