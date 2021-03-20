
# 2分查找数字，返回对应的序号    陈海滨  2021年3月6日17点35分
def find(arr, target, start_index):
    if arr is None:
        return None
    if len(arr) < 1:
        return None
    mid_index = int(len(arr) / 2)
    mid = arr[mid_index]

    if mid > target:
        # 目标值小于中点，左边查找
        return find(arr[:mid_index], target, start_index)
    elif mid == target:
        return start_index + mid_index
    else:
        # 目标值大于中点，右边查找
        return find(arr[mid_index + 1:], target, start_index + mid_index + 1)


if __name__ == "__main__":
    input_arr = [1, 3, 5, 6, 8, 12]
    target = 8
    print(find(input_arr, target, 0))






