def lengthLongSub(s):
    output = ""
    result = 0
    for index in range(0,len(s)):
        if s[index] not in output:
            output += s[index]
            if len(output) > result:
                result = len(output)
        else:
            num = output.find(s[index])
            output = output[num+1:len(output)]
            output += s[index]
    return result

input = "abcabcbb"
print(lengthLongSub(input))