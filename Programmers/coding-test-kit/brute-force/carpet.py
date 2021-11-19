def solution(brown, yellow):
    answer = []
    for row in range(brown+yellow+1,0,-1):
        if (brown+yellow)%row==0:
            column=(brown+yellow)//row
            if row-2 >0 and column-2>0:
                if (row-2)*(column-2)==yellow:
                    answer.append(row)
                    answer.append(column)
                    return answer
