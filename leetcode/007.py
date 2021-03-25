class Solution:
    def reverse(self, x: int) -> int:
        result = ''
        x_str = str(x)
        import math
        max = math.pow(2, 31) - 1
        min = (-1) * math.pow(2, 31)
        if x < min or x > max:
            return 0
        is_more = True
        if x_str[0] == '-':
            x_str = x_str[1:]
            result += '-'

        for index in range(0, len(x_str)):
            result += x_str[len(x_str) - index - 1]
        result = int(result)
        if result < min or result > max:
            return 0
        else:
            return result


if __name__ == "__main__":
    x = int('-100')
    solution = Solution()
    print(solution.reverse(x))