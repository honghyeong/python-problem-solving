def solution(phone_book):
    answer = True
    for p in range(len(phone_book)):
        for k in range(p+1,len(phone_book)):
            s=phone_book[p]
            l=phone_book[k]
            if(len(s)>=len(l)):
                break
            
            if l[:len(s)]==s:
                print(l[:len(s)],s)
                return False
    return answer