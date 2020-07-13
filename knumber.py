''' 
프로그래머스 K번째 함수구하기
'''

def solution(array, command):
    answer = []
    for i in range(len(command)):
        array_copy = array[:]
        array_copy = array[command[i][0]-1:(command[i][1])]
        array_copy.sort()
        answer.append(array_copy[command[i][2]-1])
    return answer

arrays = [1,5,2,6,3,7,4]
commands = [[2,5,3],
           [4,4,1], 
           [1,7,3]]

print(solution(arrays, commands))


