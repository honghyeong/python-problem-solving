import math

def solution(progresses, speeds):
    answer = []
    
    temp=[]
    for i in range(len(progresses)):
        temp.append(math.ceil((100-progresses[i])/speeds[i]))
        
    while temp:
        a=temp.pop(0)
        print(a)
        deploy_num=1
        while temp and temp[0]<=a:
            temp.pop(0)
            deploy_num+=1
        answer.append(deploy_num)

    return answer