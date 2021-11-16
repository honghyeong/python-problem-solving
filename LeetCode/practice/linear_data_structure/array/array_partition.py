#561
# Ascending Sort, Ascending Pair
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum=0
        pair=[]
        
        for n in nums:
            pair.append(n)
            if len(pair)==2:
                sum+=min(pair)
                pair=[]
        return sum
   
   
 # Sort, Compute even number
 class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum=0
        nums.sort()
        for i,v in enumerate(nums):
            if i%2==0: # function min always return even index value
                sum+=v
        return sum

# Pythonic way
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
