#5622
strs=input()
d=dict(ABC=3,DEF=4,GHI=5,JKL=6,MNO=7,PQRS=8,TUV=9,WXYZ=10)
sum=0
for i in strs:
    for j in d.keys():
        if i in j:
            sum+=d[j]
print(sum)
