# from collections import deque 

# '''
# BOJ - DFS/BFS
# '''

# def bfs(grahps, start):
#     visited = []
#     queue = [start] #시작노드

#     while queue:
#         n = queue.pop(0)
#         if n not in visited:
#             visited.append(n)
#             # visited = ['A']
#             queue += grahps[n] - set(visited) 
#             # queue=['A']    
#             # = ['A'] + ['B', 'C'] - ['A'] 
#             # = ['A','B','C'] - ['A']
#             # = ['B','C']
#     return visited

# def dfs(grahps, start):
#     visited = []
#     queue = [start]
#     while queue:
#         n = queue.pop()
#         if n not in visited:
#             visited.append(n)
#             queue += grahps - set(visited)
#     return visited


# NMV = map(list(int,input())

# # graph['A'] (KEY) = set[ '연결된 노드값' ] (Value)
# # graph[A] = set(['B','C'])
# for N in range(NMV[1]):
#     input()



