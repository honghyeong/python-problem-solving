#42

# Using Two Pointer : Move two pointers to maximum value
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        volume=0
        left,right=0,len(height)-1
        left_max,right_max=height[left],height[right]

        while left<right:
            left_max=max(left_max,height[left])
            right_max=max(right_max,height[right])

            #move two pointers to the highest height
            if left_max<=right_max:
                volume+=left_max-height[left]
                left+=1
            else:
                volume+=right_max-height[right]
                right-=1
        return volume
        
***      
# Using Stack
class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        volume=0

        for i in range(len(height)):
            # Meet inflection point
            while stack and height[i]>height[stack[-1]]:
                #스택에서 꺼낸다
                top=stack.pop()

                if not len(stack):
                    break
                # 이전과의 차이만큼 물 높이 처리
                distance=i-stack[-1]-1
                waters=min(height[i],height[stack[-1]])-height[top]

                volume+=distance*waters

            stack.append(i)
        return volume
