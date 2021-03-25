class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None:
            return False
        x_str = str(x)
        if len(x_str) == 1:
            return True

        mid = len(x_str) / 2
        length = len(x_str)
        for index in range(0, length):
            if index > mid:
                return True
            if x_str[index] == x_str[length-1-index]:
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    input = "12321"
    print(solution.isPalindrome(input))