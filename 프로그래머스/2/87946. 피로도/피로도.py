from itertools import permutations
def solution(k, dungeons):
    answer = 0
    arr = list(permutations(dungeons,len(dungeons)))
    for i in arr: # 실행 횟수
        now = k
        ans = 0
        for minValue ,value in i:
            if now < minValue: # 현재 피가 최소 필요도보다 작은 경우
                break # 더 할필요 없음
            now -= value # 던전 피 까고
            ans += 1
        answer = max(answer, ans)
        
            
        
    return answer