#10809

strs=input()
ans=[-1]*26
for i in strs:
    ans[ord(i)-ord('a')]=strs.find(i)
for i in ans:
    print(i,end=' ')
