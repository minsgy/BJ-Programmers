temp = list(input())
answer = 'true'

for i in range(len(temp)-1):
    if answer == 'false':
        break
    if temp[i] == '1':
	    for j in range(i+1, len(temp)):
		    if temp[j] == '1':
			    answer = 'false'
			    break

print(answer)


    		