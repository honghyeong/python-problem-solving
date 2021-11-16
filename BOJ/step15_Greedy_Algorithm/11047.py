import sys
input=sys.stdin.readline
N,K=map(int,input().split())
a=[]
result=0
for _ in range(N):
    a.append(int(input()))

for i in a[::-1]: # 오름차순으로 정렬된 동전의 리스트 중 큰 것부터 K값에서 제거해준다.  ( 최소 동전 개수를 갖기위한 greedy choice, 최대한 큰 값을 빼려는 선택 )

    if K-i>=0:  # while문 사용할 경우, 시간초과 따라서, 한 번에 현재의 K값에서 선택한 동전이 들어가는 크기를 구한다.
        div=K//i
        K=K-i*div
        result+=div

    if K==0:
        break
print(result)
