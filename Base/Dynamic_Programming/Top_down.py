#Top-down : Memoization

def fib(n):
  if n<=1:
    return n
  if dp[n]:
    return dp[n]
  
  dp[n]=fib(n-1)+fib(n-2)  ## Most important part, save the new value on default dict(dynamic programming)
  return dp[n]  ## and return
