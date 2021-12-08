def solution(bridge_length, weight, truck_weights):
    complete=len(truck_weights)
    passed=[]
    on_bridge=[]
    time=1
    cur_weight=0 # sum 대신해서 훨씬 빠름
       
    while True:
        # 다리 위에 트럭이 있고, 가장 앞에 있는 트럭이 다리를 다 건넜을 때, passed에 추가
        if(on_bridge and time-on_bridge[0][1]==bridge_length):
            arrive=on_bridge.pop(0)
            passed.append(arrive)
            cur_weight-=arrive[0]
        # 모든 트럭이 다리를 다 건넜을 때
        if(len(passed)==complete):
            answer=time
            break
        # 건널 트럭이 있고, 현재 트럭이 올라갈 수 있는지? + 다리 길이 안넘는지 
        if (truck_weights and (cur_weight+truck_weights[0])<=weight and (len(on_bridge)<bridge_length)):
            go=truck_weights.pop(0)
            cur_weight+=go
            on_bridge.append((go,time))
            
        time+=1

    return answer