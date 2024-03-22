'''

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.
'''

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        n = len(nums)

        def recursion(i,t) : 
            if t == target and i== n: 
                return 1
            if t != target and i == n :
                return 0
            if (i,t) in dp :
                return dp[(i,t)]

            dp[(i,t)] = recursion(i+1, t + nums[i]) + recursion(i+1, t - nums[i])
            return dp[(i,t)]

        return recursion(0,0)
        
# Time and space complexity is O(n*target)