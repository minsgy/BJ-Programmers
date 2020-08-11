# 배추

# 0으로 다 초기화를 하고
# 1이 든 좌표 값들을 큐에 넣기,[4,5] ... append (FIFO) count += 1
# queue에서 pop.left() = [0,0] 을 하면서 이것의 [x+1,0], [y+1,0], [x-1,0], [y-1,0] (상하좌우)에 1이 있는지 확인.
# 1이 존재 할 시, 해당 좌표 1이 든 queue에 push() 그리고 반복 한다. 주위에 1이 없을 때 까지
# if [1,0] in queue:

# 1이 주위에 없을 시, queue에 push() 되는 것이 없다. ex) [1, 1] 
# 그 때 count 값 증가, 계속 위와같이 pop.left() 해주어서 queue에 아무 좌표 없을 때까지 반복
# 그리고 count 값을 출력하면 해당 지렁이 개수가 나오게됨

def go():
    count = 0
    while queue:
        x, y = queue.pop(0)
        #[0,2] -> [1,2], [0,2], [1,1], [0,3]
        if [x+1, y] or [x-1, y] or [x, y-1] or [x, y+1] in queue:
            continue
        else:
            count += 1
    return count
            

number = int(input())
for _ in range(number):
    n, m, earthworm = map(int, input().split(' '))
    queue = [] 

    for i in range(earthworm):
        i, j = map(int, input().split(' '))
        queue.append([i, j])

    queue.sort()
    
    print(go())

