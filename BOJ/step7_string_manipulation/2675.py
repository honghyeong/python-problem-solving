#2675

N=int(input())
for _ in range(N):
    count,strs=input().split()
    count=int(count)
    result=''
    for i in strs:
        result+=i*count
    print(result)
