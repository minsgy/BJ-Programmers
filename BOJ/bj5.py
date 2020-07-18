
def search(temp):
    temp2 = list(temp) # 받아온 문자열을 리스트 형식 변환
    stack_list = [] # 임의로 저장 할 Stack List
    for i in temp2:  
        if i == '(': # '(' 일 시 push 
            stack_list.append(i) # stack list에 맨 뒤에 추가
        elif i == ')' and not stack_list: 
            # ')' 인데, stack_list가 비어 있을 경우, 더 탐색할 필요없이 'NO' 출력
            return 'NO' 
        elif i == ')': # ')' 일 시 맞는 짝을 찾았으니, 맨위 값 삭제
            stack_list.pop()

    if not stack_list: # 나온 stack list가 비어있을 시 괄호 규칙성립
        return 'YES'
    else: # stack list가 남아있을 시 괄호 규칙 오류
        return 'NO'
    


n = int(input()) # 입력받을 괄호식 개수
true_false_list = []

for i in range(n): # 입력받을 괄호식 만큼 반복
    te_mp = input()
    true_false_list.append(search(te_mp)) 
    # search 함수를 통해 나온 'YES', 'NO'값을 결과 리스트에 추가함.

for value in true_false_list: # 리스트를 출력
    print(value)


            

