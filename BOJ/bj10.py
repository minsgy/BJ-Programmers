
#bfs 문제
def go(x, y, count):
    queue = [] # 1이 들어있는 좌표값 저장
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = count #방문번지 입력
    while queue:
        x, y = queue.pop(0) # Queue의 특성 FIFO
        for i in range(4): #위, 아래, 왼쪽, 오른쪽 탐색하기
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n: # 지도밖을 나갔는지 확인하기
                if map_array[nx][ny] == 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = count

n = int(input())
map_array = [list(map(int, list(input()))) for _ in range(n)] # 맵 입력받기
visited = [[0]*n for _ in range(n)] # 방문 체크용
# house_number = []
count = 0 # 방문 횟수 및 번지

for i in range(n):
    for j in range(n):
        if map_array[i][j] == 1 and visited[i][j] == 0: # 방문하지 않았고, 지도에는 1이 존재하는가?
            count += 1 # 방문 번지 추가
            go(i, j, count)


# 단지 개수 출력
print(visited)

