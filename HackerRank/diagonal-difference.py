
def diagonalDifference(arr):
    cnt=0
    left=0
    right=0
    for row in arr:
        left+=row[cnt]
        right+=row[-1-cnt]
        cnt+=1
    return abs(left-right)

n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))
a=diagonalDifference(arr)
print(a)