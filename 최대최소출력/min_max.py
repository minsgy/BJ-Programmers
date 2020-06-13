#숫자 값을 입력 받은 후, 숫자를 출력 하고
#받아온 숫자들 중 최대값, 최소값들을 밑에 출력하시오.
a = list(map(int, input('숫자를 입력하세요 >> ').split()))
[print(a[i], "\t", end = '') for i in range(len(a))]
#b = []
#[b.append(a[i]) for i in range(len(a))]
print("\n")
MAX = max(a)
MIN = min(a)
for i in range(len(a)):
    if (a[i]==MAX):
        print("최댓값 ", end = ' ')
    elif (a[i]==MIN):
        print("최솟값 ", end = ' ')
    else:
        print("       ", end = ' ')
