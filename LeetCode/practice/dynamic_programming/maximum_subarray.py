#53
#Memoization? Tablulation?
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1] if nums[i-1]>0 else 0
        return max(nums)
      
# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum=-sys.maxsize
        cur_sum=0

        for num in nums:
            cur_sum=max(num,cur_sum+num) # 새로운 요소를 합칠때와 합치지않을 때의 최대를 비교, 더 작아지게 만드는 앞의 부분합은 합칠필요가 없다.
            best_sum=max(best_sum,cur_sum)
            
        return best_sum
