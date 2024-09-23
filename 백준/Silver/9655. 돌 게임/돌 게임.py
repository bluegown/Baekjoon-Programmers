
N = int(input())

d = dict()
d[1] = 'SK'
d[2] = 'CY'
d[3] = 'SK'
for i in range(4,N+1):
    if d[i-1] == 'SK':
        d[i] = 'CY'
    else:
        d[i] = 'SK'
    if d[i-3] == 'SK':
        d[i] = 'CY'
    else:
        d[i] = 'SK'

print(d[N])


    