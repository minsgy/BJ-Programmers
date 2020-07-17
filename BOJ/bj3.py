def solution(s):
    answer = ''  
    # 5/2 = 2
    # 4/2 = 2 [2-1], [2]
    if (len(s) / 2) % 2 == 0:
        answer = answer + s[int(len(s)/2)-1] + s[int(len(s)/2)]
    else:
        answer = answer + s[int(len(s)/2)]
    return answer

ss = "abcde"
print(solution(ss))