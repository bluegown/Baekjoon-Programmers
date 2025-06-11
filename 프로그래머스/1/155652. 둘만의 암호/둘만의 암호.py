def solution(s, skip, index):
    answer = []
    eng = []
    print(list(skip))
    for element in range(ord('a'),ord('z') + 1):
        if chr(element) not in list(skip):
            eng.append(chr(element))
            
    for i in s:
        elementIndex = eng.index(i)
        answer.append(eng[(elementIndex + index) % len(eng)])
    return ''.join(answer)