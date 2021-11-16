import sys
def solution(n, times):
    answer = 0
    
    def immigration(n,times):

        if n < len(times):
            return max(times)

        left=min(times)
        right=max(times)*n
        result = sys.maxsize

        while left<=right:

            mid=(left+right)//2
            sum=0

            for time in times:
                sum+= mid//time
                # if sum>=n:
                #     break


            if sum>=n:
                result=mid
                right=mid-1
            else:
                left=mid+1

        return result
    
    answer=immigration(n,times)
    return answer
