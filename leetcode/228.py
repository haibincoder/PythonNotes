
class Solution:
    def summaryRanges(self, nums):
        if nums is None or len(nums) < 1:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        start = nums[0]
        last = nums[0]
        result = []
        for index, item in enumerate(nums):
            if start is None or last is None:
                start = item
                last = item
            if item == last:
                continue
            if 1 == item - last:
                # 和前一个数可以组成连续数列
                last = item
            else:
                # 不能和前一个数组成连续数列
                if last == start:
                    result.append(f"{last}")
                else:
                    result.append(f"{start}->{last}")
                start = item
                last = item
            # 最后一个数特殊处理
            if 1 == len(nums) - index:
                if start == item:
                    result.append(str(item))
                else:
                    result.append(f"{start}->{item}")
        return result


if __name__ == "__main__":
    solution = Solution()
    input = [0,2,3,4,6,8,9]
    print(solution.summaryRanges(input))
