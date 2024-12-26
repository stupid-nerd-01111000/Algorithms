class Solution():
    @staticmethod
    def twoSum(nums, target):
        for num in range(len(nums) - 1):
            zz = nums[num] + nums[num + 1]
            if zz == target:
                return [num, num + 1]
        return [-1, -1]



numso = [1, 1, 3, 3, 5, 6, 7, 8, 4, 1]

targeto = 5


result = Solution.twoSum(nums=numso, target=targeto)
print(result)