
'''
Programmers - 전화번호 목록
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421

전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 
true를 return 하도록 solution 함수를 작성해주세요.

'''
def solution(phone_book):
    answer = True # 접두어가 없다는 가정하에 시작. 접두어가 존재 시 False반환
    phone_book.sort() # 정렬하게 되면, 119, 1195524421, 97674223
    for i in range(len(phone_book)-1): #총 3번의 비교 0. 1. 2
        if phone_book[i] in phone_book[i+1]: 
            #i번째가 i+1번째에 포함되어있으므로 접두어 확인
            #i와 i+1를 비교해주니까, 반복문이 i-2번까지만 반복하면 되니까 len-1 탐색
            answer = False 
            break
    return answer

phone_books = ["12", "567","1235","123","88"]
# 119, 1195524421, 97674223
# 123, 456, 789
# 12, 123, 1235, 567, 88
solution(phone_books)