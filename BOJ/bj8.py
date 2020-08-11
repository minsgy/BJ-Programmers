
n, m = map(int, input().split(' '))

tomato = [[0]*n]*m # 0으로 초기화
queue = [] # 1의 좌표를 저장ㅎ라
print(tomato)
for i in range(m):
    temp = list(map(int, input().split(' ')))
    print(temp)
    for j in range(len(temp)):
        if temp[j] == 1:
            queue.append([i, j])
    # temp = [0, 0, 0, 1]  0~3 [0,1,2,3]

print(queue)





