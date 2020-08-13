import sys

number = int(input())
str_ans = input()
nums = [0]*number

for i in range(number):
    nums[i] = int(input())

stack = []

for ch in str_ans:
    #문자 A,B,C,D,E
    if ch.isupper(): # 문자열의 대문자 여부 감지
        stack.append(nums[ord(ch)-ord('A')]) # 아스키 코드 값 반환 스택 추가
    else:
        #뒤에 stack 값 2개 빼와서 연산하기
        num2 = stack.pop()
        num1 = stack.pop()

        if ch=='+':
            stack.append(num1+num2)
        elif ch=='-':
            stack.append(num1-num2)
        elif ch=='/':
            stack.append(num1/num2)
        elif ch=='*':
            stack.append(num1*num2)

print(format(stack[0],".2f")) # 소숫점 2자리가 서식화된 문자로 반환함