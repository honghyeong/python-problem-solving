#1316
def groupchecker(a:str)->bool:
    if len(a)<=2:
        return True

    for char in a:
        if a.count(char)==1:
            continue
        else:
            h=a.find(char)
            r=a.rfind(char)
            for i in range(h+1,r):
                if char!=a[i]:
                    return False
    return True

N=int(input())
sum=0
for _ in range(N):
    a=input()
    if groupchecker(a):
        sum+=1
print(sum)
