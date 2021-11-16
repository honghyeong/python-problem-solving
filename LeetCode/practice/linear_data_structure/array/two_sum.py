#1

# Brute Force Algorithm O(n**2)
# The most inefficent algorithm.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i.j]
                    
# Using 'in' 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            complement=target-v
            if complement in nums[i+1:]:
                # find index which has complement var after index i
                return nums.index(v), nums[i+1:].index(complement)+(i+1)
                
# Using Dictionary, to find at once.            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        # save to dictionary , value->key, index->value
        for i,num in enumerate(nums):
            nums_map[num]=i
        # Search by key , complement value
        for i,num in enumerate(nums):
            if target-num in nums_map and i!=nums_map[target-num]:
                return i,nums_map[target-num]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        # save to dictionary , value->key, index->value
        for i, num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num]=i

            
