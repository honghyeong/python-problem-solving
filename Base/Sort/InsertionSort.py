N=int(input())

numbers=[]

for _ in range(N):
    numbers.append(int(input()))

# Insertion Sort

for i in range(1,len(numbers)):
    for j in range(i,0,-1):
        if numbers[j-1] > numbers[j]:
            numbers[j-1],numbers[j]=numbers[j],numbers[j-1]


for n in numbers:
    print(n)
