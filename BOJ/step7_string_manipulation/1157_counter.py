#1157
#Using counter, most_common

import collections

strs=input()
strs=strs.upper()
alp_counter=collections.Counter(strs)

if len(strs)==1:
    print(strs)
elif alp_counter.most_common(2)[0][1]==alp_counter.most_common(2)[1][1]:
    print("?")
else:
    print(alp_counter.most_common(1)[0][0])
