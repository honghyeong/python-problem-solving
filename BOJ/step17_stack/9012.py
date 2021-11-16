import sys

def isvps(s:str)->bool:
    stack=[]
    for char in s:
        if char=='(':
            stack.append(char)
        elif char==')':
            if len(stack)!=0:
                stack.pop()
            else:
                return False

    return len(stack)==0

input=sys.stdin.readline
K=int(input())

for _ in range(K):
    a=input().strip()
    if isvps(a):
        sys.stdout.write('YES'+'\n')
    else:
        sys.stdout.write('NO'+'\n')
