N=int(input())

numbers=[]

for _ in range(N):
    numbers.append(int(input()))

# Bubble Sort

for i in range(len(numbers)-1):
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

for n in numbers:
    print(n)
