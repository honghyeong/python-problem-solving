
# Using input,print
N=input()
strs=input()
sum=0
for i in strs:
    sum+=int(i)
print(sum)


# Using sys
import sys
N=sys.stdin.readline().strip()
strs=sys.stdin.readline().strip()
sum=0
for i in strs:
    sum+=int(i)
sys.stdout.write(str(sum))
