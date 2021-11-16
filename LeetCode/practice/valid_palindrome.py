#1 Invert to list
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # checking palindrome validation
        while len(strs)>1:
            if strs.pop(0)!=strs.pop():
                return False

        return True
        
#2 Using Deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs:Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False

        return True
        
        
#3 Using slicing, Regular Expression
class Solution:
    def isPalindrome(self,s: str) -> bool:
        s=s.lower()
        # using regular expression : filtering
        s=re.sub('[^a-z0-9]','',s)

        return s[:]==s[::-1]
