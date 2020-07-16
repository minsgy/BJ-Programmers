'''
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
'''
def solution(citations):
    answer = len(citations) # 전체 논문 n편 5
    citations.sort() # 오름차순 인용 논문 개수 정렬 [0 ,1, 3 ,5 ,6]
    while 1: 
        cnt =0
        for i in citations: # 논문 인용개수 0,1,3,5,6
            if i >= answer: 
                cnt+=1 # h번 이상 인용된 논문일 시 카운트
            if answer <= cnt: # h번 이상 인용된 논문이 h편 이상일 시 H-index로 인식.
                return answer # 해당 h-index 리턴
        answer-=1 # 전체 논문 하나씩 줄여서 5,4,3,2,1 인용 개수 줄이기
    return answer


# 0 1 3 5 6
citation = [3,0,6,1,5]

print(solution(citation))


