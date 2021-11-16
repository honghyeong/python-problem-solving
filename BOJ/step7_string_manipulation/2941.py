#5622
strs=input()
d=['c=','c-','dz=','d-','lj','nj','s=','z=']
result=len(strs)
for i in d:
    for _ in range(strs.count(i)):
        result-=1
print(result)

