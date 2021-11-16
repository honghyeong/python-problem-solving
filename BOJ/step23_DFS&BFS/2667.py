import collections
N=int(input())
grid=[]
for i in range(N):
    grid.append(list(input().strip()))

def dfs(i,j,count=0):

    # 더 이상 땅이 아닌 경우 종료
    if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j] != '1':
        return

    grid[i][j]='0'
    # 불변 객체를 사용할 경우, 재할당이 불가능하므로 가변객체를 사용.
    # count값을 참조했을 때, keyvalue error가 생겨날 것을 방지해서 defaultdict사용
    numbers[count]+=1 

    # count로 몇 번째 단지묶음 인지 전달.
    dfs(i+1,j,count)
    dfs(i-1,j,count)
    dfs(i,j+1,count)
    dfs(i,j-1,count)


numbers=collections.defaultdict(int)
a=0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='1':
            dfs(i,j,a) # dfs(row,column,몇 번째 단지?)
            a+=1


numbers=list(numbers.values()) # 리스트로 변경
numbers.sort() # 오름차순 정렬
print(len(numbers))
for i in numbers:
    print(i)
