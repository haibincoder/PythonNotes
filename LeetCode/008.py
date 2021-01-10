class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '-':
            return 0
        if len(s) < 1:
            return 0
        valid_str = s.split(' ')
        for item in valid_str:
            if len(item) > 0:
                s = item
                break

        valid = ['-', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nums = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


        result = ''
        s = s.replace(' ', '')
        if len(s) > 2:
            if s[0] not in nums and s[1] not in nums:
                return 0

        is_float = False
        for index, char in enumerate(s):
            if char == '.':
                break
            if char in valid:
                result += char
            elif char == ' ':
                continue
            else:
                if len(result) < 1:
                    if char == '+':
                        continue
                    return 0
                elif result[0] == '-' and len(result) < 2:
                    return 0
                else:
                    break

        if len(result) < 1:
            return 0

        if result[len(result) - 1] == '-':
            result = result[:len(result)-1]
        try:
            if is_float:
                result = float(result)
            else:
                result = int(result)
            import math
            max = int(math.pow(2, 31) - 1)
            min = int(math.pow(2, 31) * (-1))

            if result > max:
                return max
            elif result < min:
                return min
            else:
                return result
        except Exception as ex:
            return 0


if __name__ == "__main__":
    solution = Solution()
    input = '.1'
    print(solution.myAtoi(input))