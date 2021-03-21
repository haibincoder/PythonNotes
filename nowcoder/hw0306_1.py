
# 陈海滨 2021年3月6日14点58分

def find(input_str):
    if input_str is None:
        return -1
    if len(input_str) < 1:
        return 0

    max_length = 0
    max_index = 0
    current_length = 0
    last_num = None

    for index in range(len(input_str)):
        item = input_str[index]
        if not item.isdigit():
            current_length = 0
            last_num = None
            continue
        else:
            item = int(item)
            if last_num is None:
                current_length = 1
                last_num = item
            elif item == last_num + 1:
                current_length += 1
                last_num = item

                if current_length >= max_length:
                    max_length = current_length
                    max_index = index - max_length + 1
            else:
                current_length = 1
                last_num = None

    return (max_index, max_length)



if __name__ == "__main__":
    input_str = 'abcd12345ed125ss123456'

    print(find(input_str))
