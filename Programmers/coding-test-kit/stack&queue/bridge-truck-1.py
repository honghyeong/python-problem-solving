def solution(bridge_length, weight, truck_weights):
    sort_arr=sorted(truck_weights)
    passed=[]
    on_bridge=[]
    time=1
    cur_weight=0
    # print(sort_arr)
    while time<5:
        
        if(on_bridge and time-on_bridge[0][1]==bridge_length):
            passed.append(on_bridge.pop(0))
            if(len(passed)==len(truck_weight)):
                break
        
        if(cur_weight+sort_arr[0]<=weight):
            go=sort_arr.pop(0)
            print('go:',go)
            cur_weight+=go
            on_bridge.append((go,time))
            
        
        time+=1
        print('')
        print('onbridge:',on_bridge)
        print('passsed:',passed)
        print('time:',time)
    answer = 0
    return answer