# Brute-Force Recursive
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
      
# Memoization : Top-Down
# 하위 문제에 대한 정답을 계산했는지 확인해가며 문제를 자연스럽게 재귀 방식으로 풀어나간다. 
# 단, 기존 재귀 풀이와 거의 동일하면서도 이미 풀어봤는지 확인하여 재활용하는 효율적인 방식이다.
class Solution:

    dp=collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n<=1:
            return n
        if self.dp[n]:
            return self.dp[n]  # Recycle - Efficient

        self.dp[n]=self.fib(n-1)+self.fib(n-2) # Recursive 
        return self.dp[n]
      
# Tablulation : Bottom-up
# tablulation - 작은 하위 문제부터 살펴보고, 작은 문제의 정답을 이용해 큰 문제의 정답을 풀어나간다. 
class Solution:

    dp=collections.defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[1]=1

        for i in range(2,n+1):
            self.dp[i]=self.dp[i-1]+self.dp[i-2]
        return self.dp[n]
      
      
      
# Two variables ; tc O(n), sc O(1)
class Solution:
    def fib(self, n: int) -> int:
        x,y=0,1
        for i in range(0,n):
            x,y=y,x+y
        return x
      
      
