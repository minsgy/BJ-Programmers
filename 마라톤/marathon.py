#기본 코드

#exp1
'''
participants = ['leo', 'kiki', 'eden']
completions = ['eden', 'kiki']
'''
#exp2
'''
participants = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completions = ['marina', 'josipa', 'nikola', 'filipa']
'''
#exp3
participants = ['mislav', 'stanko', 'mislav', 'ana']
completions = ['mislav', 'stanko', 'ana']


#참가자 명단에 포함된 갯수와, 완주자 명단에 포함된 갯수 딕셔너리{이름:[참가자, 완주자]}
dic = {}
    #딕셔너리 초기화
for i in participants:
    dic[i] = [0,0]
    #참가자 명단의 수 입력
for i in participants:
    dic[i][0] += 1
    #완주자 명단의 수 입력
for i in completions:
    dic[i][1] += 1

#참가자 명단의 수와 완주자 명단의 수 비교하여 누가 완주하지 못했는지 출력
for i in dic:
    #참가자 명단의 수 > 완주자 명단의 수
    if dic[i][0] > dic[i][1]:
        #참가자 명단의 수가 두명 이상일 경우
        if dic[i][0] >= 2:
            print('{}는 참가자 명단에는 두명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.'.format(i))
        #참가자 명단 한명일경우
        else:
            print("{}는 참가자 명단에는 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.".format(i))