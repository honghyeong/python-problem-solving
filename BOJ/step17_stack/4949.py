import sys

def isbalanced(s:str)->bool:
    stack=[]
    table={'(':')','[':']'}
    for char in s:
        if char in table:
            stack.append(char)
        elif char in table.values():
            if not stack or char!=table[stack.pop()]:
                return False

    return len(stack)==0

input=sys.stdin.readline

while True:
    a=input().rstrip()
    if a=='.':
        break
    if isbalanced(a):
        sys.stdout.write('yes'+'\n')
    else:
        sys.stdout.write('no'+'\n')
