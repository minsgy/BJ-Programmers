temp = input().split()
temp2 = temp[:]
answer = 'true'

temp.sort()
max_temp = max(temp)


if int(max_temp) > 45:
    answer ='false'

elif temp2 == temp:
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            answer = 'false'
            break
else:
    answer = 'false'    

print(answer)


    		