def miniMaxSum(arr):

    arr.sort()
    print(sum(arr)-arr[-1],end=' ')
    print(sum(arr)-arr[0])


arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)

