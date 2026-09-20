def change_to_two(num, n):
    ans = []
    while num >= 1:
        ans.append(str(num % 2))
        num = num // 2
    while len(ans) < n:
        ans.append('0')
    return ''.join(ans[::-1])
        
def solution(n, arr1, arr2):
    answer = []
    graph = []
    for i in range(n):
        ans = ''
        st1 = change_to_two(arr1[i], n) 
        st2 = change_to_two(arr2[i], n) 
        for j in range(n):
            if st1[j] == '0' and st2[j] == '0':
                ans += ' '
            else:
                ans += '#'
        graph.append(ans)

    return graph