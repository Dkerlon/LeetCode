class Solution(object):
    def runningSum(self, nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums

solucao = Solution()

print(solucao.runningSum([1,2,3,4,5,6]))