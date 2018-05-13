# left: the first index of array
# right: the last index of array
def quick_sort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        quick_sort(array, left, q - 1)
        quick_sort(array, q + 1, right)

def partition(array, left, right):
    x = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


array = [2, 4, 6, 2, 0, 63, 12, 56, 45, 6, 34, 6, 32, 23, 54, 4]
print(array)
quick_sort(array, 0, len(array) - 1)

print(array)
