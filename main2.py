"""
客服系统的模糊音纠错函数，输入拼音字符串，声母常见混淆为 r l n不分，zh、z不分。韵母常见前后鼻音混淆，ang、an不分，给定一个拼音为输入，生成其对应的混淆组合候选
常见的混淆韵母有ang, eng, ing, uang, ong
常见的翘舌有 zh-z, ch->c, sh->s
常见的声母有 r,l,n

例如：
用户输入"zhang"
代码输出"{zan, zang,zhan,zhang}"

用户输入"ren"
代码输出"{ren, len, nen, reng, leng, neng}"

"""

correct_list1 = ['r', 'l', 'n']

# 前缀匹配
correct_dic1 = {'zh': 'z', 'ch': 'c', 'sh': 's'}
correct_dic2 = {value: key for key, value in correct_dic1.items()}
correct_dic_pre = {**correct_dic1, **correct_dic2}

# 后缀匹配
correct_dic1 = {'ang': 'an', 'eng': 'en', 'ing': 'in', 'uang': 'uan', 'ong': 'on'}
correct_dic2 = {value: key for key, value in correct_dic1.items()}
correct_dic_end = {**correct_dic1, **correct_dic2}


def correct(input_str):
    result = [input_str]
    # 替换list
    for item in correct_list1:
        if input_str.startswith(item):
            for item_correct in correct_list1:
                tmp = input_str.replace(item, item_correct)
                if tmp in result:
                    continue
                result.append(tmp)
    # 前缀替换
    for item_str in result:
        for item in correct_dic_pre:
            if item_str.startswith(item):
                tmp = item_str.replace(item, correct_dic_pre[item])
                if tmp in result:
                    continue
                result.append(tmp)
    # 后缀替换
    for item_str in result:
        for item in correct_dic_end:
            if item_str.endswith(item):
                tmp = item_str.replace(item, correct_dic_end[item])
                if tmp in result:
                    continue
                result.append(tmp)
    return result


if __name__ == "__main__":
    input_str = 'ren'
    print(correct(input_str))