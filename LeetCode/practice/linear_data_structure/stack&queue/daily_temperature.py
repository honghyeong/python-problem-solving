#739

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        answer=[0]*len(T)
        stack=[]
        for i,cur in enumerate(T):

            # if current temperature is higher than stack value
            while stack and cur>T[stack[-1]]:
                idx=stack.pop()
                answer[idx]=i-idx

            stack.append(i)
        return answer
