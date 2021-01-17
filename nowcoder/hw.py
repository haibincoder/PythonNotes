

"""
题目：找出字符串中长度最大的子串，如果子串长度相同，输出ascii最小的子串
输入:  aaacccczzzz
输出: cccc
"""

if __name__ == "__main__":
    input_str = input()

    input_str = input_str.replace(' ', '')

    if input_str is None or len(input_str) < 1:
        print('')
    else:
        max_count = 0
        max_count_char = None
        last_char = None
        last_count = 0
        for index, item_char in enumerate(input_str):
            if last_char is None:
                last_char = item_char
                last_count = 0
                max_count_char = item_char
                max_count = 1

            if item_char == last_char:
                last_count += 1
                if last_count > max_count:
                    max_count = last_count
                    max_count_char = last_char
                elif last_count == max_count and ord(last_char) <= ord(max_count_char):
                    max_count = last_count
                    max_count_char = last_char
            else:
                last_char = item_char
                last_count = 1
                if last_count > max_count:
                    max_count = last_count
                    max_count_char = last_char
                elif last_count == max_count and ord(last_char) <= ord(max_count_char):
                    max_count = last_count
                    max_count_char = last_char
        result = ''
        for index in range(max_count):
            result += max_count_char
        print(result)