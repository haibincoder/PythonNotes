"""
题目描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。
输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)
结果 （10， -10）
注意请处理多组输入输出
输入描述:
一行字符串
输出描述:
最终坐标，以逗号分隔
"""


def valid(input_str, valid_char):
    if input_str is None or len(input_str) < 1 or input_str[0] not in valid_char:
        return False
    try:
        temp = int(input_str[1:])
        if temp > 0:
            return True
        else:
            return False
    except Exception as ex:
        return False

if __name__ == "__main__":
    input_arr = []
    valid_char = ['W', 'A', 'S', 'D']

    item_list = input().split(';')
    for item_str in item_list:
        if valid(item_str, valid_char):
            input_arr.append(item_str)

    loc = [0, 0]
    for item in input_arr:
        start = item[0]
        length = int(item[1:])
        if start == 'W':
            loc[1] = loc[1] + length
        elif start == 'S':
            loc[1] = loc[1] - length
        elif start == 'A':
            loc[0] = loc[0] - length
        elif start == 'D':
            loc[0] = loc[0] + length

    print(f'{loc[0]},{loc[1]}')

