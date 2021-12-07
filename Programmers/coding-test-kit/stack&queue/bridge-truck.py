def solution(bridge_length, weight, truck_weights):
    exit=len(truck_weights)
    # print('truck_weights:',truck_weights)
    passed=[]
    on_bridge=[]
    time=1
    cur_weight=0
       
    while True:

        if(on_bridge and time-on_bridge[0][1]==bridge_length):
            arrive=on_bridge.pop(0)
            passed.append(arrive)
            cur_weight-=arrive[0]

        if(len(passed)==exit):
            answer=time
            break
            
        if (truck_weights and (cur_weight+truck_weights[0])<=weight and (len(on_bridge)<bridge_length)):
            go=truck_weights.pop(0)
            cur_weight+=go
            on_bridge.append((go,time))
            
#         print('onbridge:',on_bridge)
#         print('passsed:',passed)
#         print('time:',time)
#         print(len(passed))
        time+=1

    return answer