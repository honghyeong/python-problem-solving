import sys
import math
N=int(sys.stdin.readline())
eratos=[0]+[1]*N
eratos[1]=0
valid_prime=[]
result=0
for i in range(2,int(math.sqrt(N))+1):
    for j in range(i*2,N+1,i):
        eratos[j]=0 # eratosthenes' sieve

for i,v in enumerate(eratos):
    if v:
        valid_prime.append(i) # list of prime numbers which are smaller than N

sum_arr=[0] # to operate sum opeartion in O(1) time complexity, use sum_arr
sum=0
for i in range(len(valid_prime)):
  sum+=valid_prime[i]
  sum_arr.append(sum)

# using two pointer to find partition sum ( successive )
left=0
right=1
while left!=len(valid_prime):
  if sum_arr[right]-sum_arr[left]>N: # *** Keep warning ***
    left+=1
  elif sum_arr[right]-sum_arr[left]<N:
    if right==len(valid_prime):
        left+=1
    else:
        right+=1
  else:
    result+=1
    left+=1 # find another result
    right+=1
sys.stdout.write(str(result))
