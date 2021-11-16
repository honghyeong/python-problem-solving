#344

#1 : two pointer swap
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left,right=0,len(s)-1
        
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

            
#2 : Pythonic way : reverse function
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
