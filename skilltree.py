'''
선행 스킬이란 어떤 스킬을 배우기 전에 먼저 배워야 하는 스킬을 뜻합니다.

예를 들어 선행 스킬 순서가 스파크 → 라이트닝 볼트 → 썬더일때, 
썬더를 배우려면 먼저 라이트닝 볼트를 배워야 하고, 라이트닝 볼트를 배우려면 먼저 스파크를 배워야 합니다.

위 순서에 없는 다른 스킬(힐링 등)은 순서에 상관없이 배울 수 있습니다. 
따라서 스파크 → 힐링 → 라이트닝 볼트 → 썬더와 같은 스킬트리는 가능하지만,
 썬더 → 스파크나 라이트닝 볼트 → 스파크 → 힐링 → 썬더와 같은 스킬트리는 불가능합니다.

선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질 때, 
가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

'''
def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)#C,B,D 분리
    # BACDE일 때, C,B,D를 제외한 모든 리스트를 제외하고, 다른 리스트에 CBD 문자 값 저장 
    # 요소 순서가 CBD가 아닐 경우, ANSWER 값을 세지않음.
    # skill_list(CBD)와 CBD를 제외하여 순서 그대로 임의 저장한 value_list를 비교합니다.
    # 순서가 맞지 않으면 break 후 False 값을 주어서, 기본값인 True일 시 가능한 스킬트리 값을 증가시킵니다.
    
    for value_skill_tree in skill_trees: # 검사할 스킬트리 반복
        value_list = [] # 각 스킬트리 구분 후 저장하는 리스트, 매번 초기화하기
        temp = list(value_skill_tree) # [B,A,C,D,E] 리스트로 분할, [C,B,A,D,F] 등
        true_false = True; # 한 리스트요소 검사 후 다시 True로 초기화
        
        for value in temp: 
            #Skill_list에 해당되지 않는 상관없는 값을 제외 후 임의 리스트에 저장.
            if value in skill_list:
                value_list.append(value) 
        n=0 # skill_list 순서구분을 위한 index 변수
        for value2 in value_list:
            if value2 == skill_list[n]:
                n+=1 # 스킬트리 맞을 시, 다음 스킬트리 검사를 위한 index 증가
            else:
                true_false = False # 순서가 맞지 않을 시 false
                break # 바로 반복문 탈출
        if true_false == True: #초기값인 True일 시, 가능한 스킬트리 이므로 개수증가
            answer+=1 # 스킬트리 개수 증가
    return answer # 가능한 스킬트리 개수 반환

skills = "CBD"
skill_tree = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skills, skill_tree))