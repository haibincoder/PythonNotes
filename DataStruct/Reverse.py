import copy

list = []
list.append(30)
list.append(20)
list.append(10)

# list2 = copy.deepcopy(list)
list2 = list.copy()

print("list1: ",list)
list.reverse()
print("list1:",list)
print("list2:",list2)
list2.sort()
print("list2:",list2)
list2.sort(reverse=True)
print("list2:",list2)