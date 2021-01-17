def solution(progresses, speeds):
    answer = []
    num=0
    ans=0
    while progresses:
        if progresses[0]+num*speeds[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            ans+=1
        else :
            if ans!=0 :
                answer.append(ans)
                ans=0
            num+=1
    answer.append(ans)
            
    return answer