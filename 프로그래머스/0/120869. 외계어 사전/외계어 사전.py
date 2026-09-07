def solution(spell, dic):
    answer = 0
    for i in dic:
        d = dict()
        
        for j in i:
            d[j] = d.get(j,0) + 1
        boolean = True
        for j in spell:
            print(d.get(j))
            if d.get(j) != 1:
                boolean = False
        if boolean:
            return 1
                
                
    
        
        
    return 2