'''
BJ - 핸드폰 요금
동호는 새악대로 T 통신사의 새 핸드폰 옴머나를 샀다. 
새악대로 T 통신사는 동호에게 다음 두 가지 요금제 중 하나를 선택하라고 했다.

영식 요금제
민식 요금제

영식 요금제는 30초마다 10원씩 청구된다.
이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 
만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 
이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 
만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면
어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오.

'''
import sys
def MS(time):
    
    money1 = [] # 민식
    money2 = [] # 영식
    for i in time:
        if(i % 60 != 0):
            temp = 15 * (int(i / 60)) + 15
            money1.append(temp)
        else:
            temp = 15 * (int(i / 60)) + 15
            money1.append(temp)
    print(money1)
    result1 = sum(money1)

    for i in time:
        if(i % 30!= 0):
            temp = 10 * (int(i / 30)) + 10
            money2.append(temp)
        else:
            temp = 10 * (int(i / 30)) + 10
            money2.append(temp)
    print(money2)        
    result2 = sum(money2)

    if(result1 < result2):
        print('M',end=' ')
        return result1 
    elif(result1 > result2):
        print('Y',end=' ')
        return result2
    else:         
        print('Y M',end=' ')
        return result1



call_timer = []

call_number = int(input())
if(call_number<=20):
    call_timer = list(map(int,input().split()))
    for i in call_timer:
        if i > 10000 or i<=0:
            sys.exit(1)
    if not call_timer[call_number:]:
        print(MS(call_timer))