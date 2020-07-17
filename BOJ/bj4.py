'''
도시에는 N개의 빌딩이 있다.
빌딩 관리인들은 매우 성실 하기 때문에, 다른 빌딩의 옥상 정원을 벤치마킹 하고 싶어한다.
i번째 빌딩의 키가 hi이고, 모든 빌딩은 일렬로 서 있고 오른쪽으로만 볼 수 있다.
i번째 빌딩 관리인이 볼 수 있는 다른 빌딩의 옥상 정원은 i+1, i+2, .... , N이다.
그런데 자신이 위치한 빌딩보다 높거나 같은 빌딩이 있으면 그 다음에 있는 모든 빌딩의 옥상은 보지 못한다.
예) N=6, H = {10, 3, 7, 4, 12, 2}인 경우

1번 관리인은 2, 3, 4번 빌딩의 옥상을 확인할 수 있다.
2번 관리인은 다른 빌딩의 옥상을 확인할 수 없다.
3번 관리인은 4번 빌딩의 옥상을 확인할 수 있다.
4번 관리인은 다른 빌딩의 옥상을 확인할 수 없다.
5번 관리인은 6번 빌딩의 옥상을 확인할 수 있다.
6번 관리인은 마지막이므로 다른 빌딩의 옥상을 확인할 수 없다.
'''
import sys
input = sys.stdin.readline

number = int(input())
building = []

for i in range(number):
    temp = int(input())
    building.append(temp)

# 해당 식은 stack을 사용하지 않아 시간초과 발생.
index = 0 # 해당 빌딩 번호
cnt = 0 # t
for height in building:
    for j in range(1+index, len(building)):
        if height > building[j]:
           cnt += 1
        elif height <= building[j]:# 위치한 빌딩보다 큰 경우,
            break
    index += 1

print(cnt) # 되는 cnt값 
