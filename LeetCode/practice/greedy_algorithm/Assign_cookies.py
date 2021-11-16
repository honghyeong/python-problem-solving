# 455
# grid factor : 일단 쿠키줘봐, 거절해? 그럼 더 큰거. 라는 느낌.
# 따라서, 작은것부터 큰 쿠키를 주는 그리디 알고리즘을 구현
# child가 만족하면 child 수 +1


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_i=cookie_j=0

        # 만족하지 못할 때 까지 그리드 진행
        while child_i<len(g) and cookie_j<len(s):
            if g[child_i]<=s[cookie_j]:
                child_i+=1
            cookie_j+=1

        return child_i
      
# 이진 검색 활용
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result=0
        for i in s:
        # 이진 검색으로 더 큰 인덱스 검색
            index=bisect.bisect_right(g,i)
            if index>result:
                result+=1
        return result
