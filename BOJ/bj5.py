'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 
한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
'''

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


            

