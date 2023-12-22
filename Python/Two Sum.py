class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]
                

    def twoSumImproved(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)): 
            complement = target - nums[i]
            if complement in hashmap:
                print(i, hashmap[complement])
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


sol = Solution()
sol.twoSum([2,7,11,15], 9)
sol.twoSumImproved([2,7,11,15], 9)

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
