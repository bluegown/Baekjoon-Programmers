def solution(bandage, health, attacks):
    answer = 0
    max_time = attacks[-1][0] # 몬스터의 마지막 공격 시간
    # 시전 시간, 초당 회복량,추가 회복량
    time = 0
    t,x,y = bandage[0],bandage[1], bandage[2]
    con_success = 0
    
    attacks = attacks[::-1]
    max_health = health
    
    attack_time , damage = attacks.pop()
    
    while time < max_time:
        damaged_yn = False
        time += 1 # 시간이 흘러가요~
        con_success += 1 # 연속 시간 측정
        if health <= 0:
            return -1
        if time == attack_time: # 공격 타이밍이라면?
            health -= damage
            print(attack_time, damage , "여기에요!!")
            con_success = 0
            damaged_yn = True
            if attacks:
                attack_time, damage = attacks.pop() # 다음 공격 타이밍 미리 꺼내둔다
        if health < max_health and not damaged_yn:
            health += x # 1초 디폴트 체력 x만큼 회복 추가
        if con_success >= t and not damaged_yn:
            health += y # t초 연속 붕대감기 성공 > y만큼 체력 추가
            con_success = 0
        health = min(health , max_health) # 기본체력 못넘게 설정
    
        
    if health <= 0:
        return -1
    return health