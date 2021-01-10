class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        list_z = [None] * numRows
        for index in range(0, numRows):
            list_z[index] = []

        item_len = 2 * numRows - 2
        for index, value in enumerate(s):
            temp = index % item_len
            if temp < numRows:
                # 每一列填满
                list_z[temp].append(value)
            else:
                # 一列只填一个值
                sub_index = (temp + 1 - numRows) % numRows
                list_z[numRows - sub_index -1].append(value)

        result = ''
        for item in list_z:
            for sub_item in item:
                result += sub_item
        return result


if __name__ == "__main__":
    solution = Solution()
    input = 'A'
    row = 2
    print(solution.convert(input, row))
