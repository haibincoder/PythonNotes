# url: https://www.nowcoder.com/practice/a35ce98431874e3a820dbe4b2d0508b1?tpId=37&tqId=21224&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking

'''
题目描述
写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字母，然后输出输入字符串中该字母的出现次数。不区分大小写。

输入描述:
第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字母。

输出描述:
输出输入字符串中含有该字符的个数。
'''

if __name__ == "__main__":
    input_str = input()
    input_char = input()
    input_char_upper = input_char.upper()

    count = 0
    for item_char in input_str:
        if item_char.upper() == input_char_upper:
            count += 1

    print(count)