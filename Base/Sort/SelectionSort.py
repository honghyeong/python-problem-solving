N=int(input())

numbers=[]

for _ in range(N):
    numbers.append(int(input()))

# Selection Sort

for i in range(len(numbers)-1): # n-1개 만 정렬하면, 나머지 1개는 자동 정렬
    maxIdx=i
    for j in range(i+1,len(numbers)):
        if numbers[j] < numbers[maxIdx]:    # 가장 작은 값 탐색
            maxIdx=j
    numbers[i],numbers[maxIdx]=numbers[maxIdx],numbers[i]

for n in numbers:
    print(n)
