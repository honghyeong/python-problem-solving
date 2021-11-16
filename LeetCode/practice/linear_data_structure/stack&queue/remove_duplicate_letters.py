#316

# Recursive Solution
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # sorted by set

        for char in sorted(set(s)):

            suffix = s[s.index(char):]

            # if set(suffix) == set(s) : devide

            if set(s) == set(suffix):
                return char+self.removeDuplicateLetters(suffix.replace(char,''))

        return ''
        
# Stack Solution   
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter,seen,stack=collections.Counters(s),set(),[]

        for char in s:
            counter[char]-=1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char<stack[-1] and counter[stack[-1]] >0:
                seen.remove(stack.pop)
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
