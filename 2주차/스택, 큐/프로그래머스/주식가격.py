def solution(prices):
    answer = []
    length=len(prices)
    for i in range(length):
        num=0
        for j in range(i+1,length):
            num+=1
            if prices[j]<prices[i]:
                break
        answer.append(num)
    
    return answer