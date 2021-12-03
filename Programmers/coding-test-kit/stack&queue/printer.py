# O(n^2) solution
# 단순한 알고리즘 구현
# priorities queue의 가장 앞이 배열의 max값이면 pop, 아니면 pop & append
# mark 는 똑같이 행동하며, target이 나올때 상황 종료.


def solution(priorities, location):
    answer = 0
    
    mark=[0]*len(priorities)
    mark[location]=1
    
    while priorities:
        if max(priorities)==priorities[0]:
            answer+=1
            priorities.pop(0)
            if(mark.pop(0)):
                break
            
#             print('print !')
#             print('priorities',priorities)
#             print('mark',mark)
            
        else:
            priorities.append(priorities.pop(0))
            mark.append(mark.pop(0))
            # print('postpone !')
            # print('priorities',priorities)
            # print('mark',mark)
        
    
    return answer