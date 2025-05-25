import sys
sys.setrecursionlimit(10000)

def find(check, rooms):
    if check not in rooms.keys():
        rooms[check] = check + 1
        return check
    empty = find(rooms[check],rooms) # 빈방을 찾을때까지 재귀 돌려버리고 발견시 check return
    rooms[check] = empty + 1 # 빈방 다음 방을 부모노드로 지정함
    return empty
        
    
def solution(k, room_number):
    answer = []
    rooms = dict()
    
    for i in room_number:
        check_in = find(i,rooms)
        
    
    return list(rooms.keys())