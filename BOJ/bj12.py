# BOJ 1050번 - 물약

dic = {}
dic2 = {}
value_list_result=[]
a, b = map(int,input().split(' '))

for _ in range(a):
    key, value = input().split(' ')
    value = int(value)
    dic[key] = value

print(dic)

for _ in range(b):
    temp = input().split('=')
    value_list = temp[1].split('+') # 3WATER, 2ADSF
    for value in value_list: #"3WATER"
        if value[0].isalpha(): #
            value_temp = int(value[0])
        if value in value_list: # 위에 만든 dic 값에 들어있는 지를 확인
            
    dic2[temp[0]] = 

