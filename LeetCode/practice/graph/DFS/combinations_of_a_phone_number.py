from typing import *

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index,path):
            # 끝까지 탐색하면 백트래킹
            if len(path)==len(digits):
                result.append(path)
                return
            
            # digits의 자릿수에 따라 그에 상응하는 문자들 차례대로 이어붙임.
            for j in dic[digits[index]]:
                dfs(i+1,path+j)
                        
        # 예외 처리
        if not digits:
            return []
        
        dic={"2":"abc","3":"def","4":"ghi","5":"jkl",
             "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        result=[]
        dfs(0,"")
        
        return result
    
