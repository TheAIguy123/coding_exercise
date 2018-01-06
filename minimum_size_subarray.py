'''
source:
https://leetcode.com/problems/minimum-size-subarray-sum/description/

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

more practice: https://leetcode.com/problems/minimum-size-subarray-sum/description/#
'''

''' IDEA 
two pointers start, end 
res = 0 
increase end until sum >= s, save len 
increase start until sum < s, save len + 1

save best_len during the process 
'''


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        best_len = 0x7fffffff # maximum 32-bit integer
        if len(nums) == 0: return 0
        s = start = end = 0 
        if sum(nums) < target: return 0 
        while end < len(nums):
            while s < target and end < len(nums):
                s += nums[end]
                end += 1 
            # if end < len(nums):
            #     best_len = min(best_len, end - start + 1)
            while s >= target:
                s -= nums[start]
                start += 1
            best_len = min(best_len, end - start + 1)
        return best_len 

        


tests = [ ([2,3,1,2,4,3], 7, 2), 
        ([], 2, 0),
        ([1, 2], 2, 1),
        ([1, 2, 3, 4,5 ,6, 7, 1, 2], 7, 1),
        ([1], 2, 0),
          ]


for test in tests:
    out = Solution().minSubArrayLen(test[1], test[0])
    assert out == test[-1], "incorrect in " + str(test) + ", out = " + str(out)

print "All tests passed!"
