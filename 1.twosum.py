
nums = [2,4,7,11,15,0,3,4]
target = 9

class Solution:
    def twoSum(self, nums, target):
        Hashtable = {}
        for i,j in enumerate(nums):
            Hashtable[j] = i
        for k in range(len(nums)):
            s = Hashtable.get(target - nums[k])
            if s != k and s is not None:
                return [k, s]


print(Solution().twoSum(nums,target))