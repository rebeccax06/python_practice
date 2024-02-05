"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
print("Welcome to my twoSum program!")
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #slower solution:
        # for x in range(len(nums)):
        #     for y in range(x+1,len(nums)):
        #         if nums[x] + nums[y] == target:
        #             return [x,y]
        seen = {}
        for x in range(len(nums)):
            diff = target - nums[x]
            if diff in seen:
                return [seen[diff],x]
            else:
                seen[nums[x]] = x

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
