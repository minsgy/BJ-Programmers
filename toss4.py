temp = input().split(' ')
stack = []

for answer in temp:
    if answer in stack:
        stack.remove(answer)
        stack.append(answer)
    else:
        stack.append(answer)

    for i in stack[:-6:-1]:
        print(i, end=' ')
    print()
