#15

# Brute Force Algorithm - Time Limit Exceeded
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()

        #Brute Force n**3
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:    #skip same value
                continue
            for j in range(i+1,len(nums)-1):
                if j>i+1 and nums[j]==nums[j-1]:    #skip same value
                    continue
                for k in range(j+1,len(nums)):
                    if k>j+1 and nums[k]==nums[k-1]:    #skip same value
                        continue
                    if nums[i]+nums[j]+nums[k]==0:
                        result.append((nums[i],nums[j],nums[k]))

        return result

# Two Pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.sort()
        for i in range(len(nums)-2): # one standard i
            if i>0 and nums[i]==nums[i-1]: # Skip duplicated value
                continue
            left=i+1 # Two Pointer
            right=len(nums)-1 # Two Pointer

            while left<right:
                sum = nums[left] + nums[right] + nums[i]

                if sum > 0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    results.append((nums[i],nums[left],nums[right])) 
                    # find answer, but combination of same values that sum==0 and skip
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    # move one step to terminate while 
                    left+=1
                    right-=1
        return results
