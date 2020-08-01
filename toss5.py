Gim = []
Lee = []
temp_list = []

Gim = list(map(int, input().split(' ')))
Lee = list(map(int, input().split(' ')))

gim_money = 0

for i in range(len(Gim)):
    if (Lee[i]+gim_money) >= Gim[i]:
        gim_money += Lee[i] - Gim[i]
        temp_list.append
    else:
        if Gim[i] >= (Lee[i]+gim_money):
            temp_list.append(Gim[i] - (Lee[i]+gim_money))
            gim_money       
        else:
            temp_list.append(0)

print(temp_list)    