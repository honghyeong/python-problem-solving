def solution(prices):
    
    stack=[]
    answer = [0]*len(prices)
    
    stack.append((prices[0],0))
    for index,price in enumerate(prices[1:]):
        while stack and stack[-1][0]>price:
            temp=stack.pop()[1]
            answer[temp]=(index+1)-temp
        
        stack.append((price,index+1))
        
        
    while stack:
        temp=stack.pop()[1]
        answer[temp]=len(prices)-(1+temp)      
    
    return answer