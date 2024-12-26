class Solution():
    @staticmethod
    def twoSum(nums, target):
        for num in range(len(nums) - 1):
            for num2 in range(num + 1, len(nums)):
                if nums[num] + nums[num2] == target:
                        return [num, num2]
        return [-1, -1]


numso = [3, 2, 3]

targeto = 6


result = Solution.twoSum(nums=numso, target=targeto)
print(result)