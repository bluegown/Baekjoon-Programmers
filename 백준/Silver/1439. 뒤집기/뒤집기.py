
s = input()
zero = 0
one = 0

if s[0] == '1':
    one += 1
else:
    zero += 1

for i in range(len(s)-1):
    if s[i]!= s[i+1]:
        if s[i+1] == '1':
            one += 1
        else:
            zero += 1
        

    
print(min(zero,one))

    
