# # 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# graph = {
#     1: [2, 5, 9],
#     2: [1, 3],
#     3: [2, 4],
#     4: [3],
#     5: [1, 6, 8],
#     6: [5, 7],
#     7: [6],
#     8: [5],
#     9: [1, 10],
#     10: [9]
# }
# visited = []

# 1. 시작노드(루트노드)인 1부터 탐색
# 2. 현재 방문한 노드를 visited_array에 추가
# 3. 현재 방문한 노드와 인접한 노드 중   방문하지 않은 노드에 방문

# def dfs_recursion(adjacent_graph, cur_node, visited_array):
#     visited_array.append(cur_node)      #1          visited_array = [1]
#     for adjacent_node in adjacent_graph[cur_node]:    #adjacent_node - 인접 노드 가져오기
#         if adjacent_node not in visited_array:          #visited_array에 인접한 노드가 없다면 재귀함수 호출   + (여기가 탈출조건)
#             dfs_recursion(adjacent_graph, adjacent_node, visited_array)

#     return


# dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
# print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!

#############재귀함수 DFS


############스택 DFS
# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


# 1. 시작 노드를 스택에 넣기
# 2. 현재 스택의 노드를 빼서 visited에 추가
# 3. 현재 방문한 노드와 인접한 노드 중에서 방문하지 않은 노드를 스택에 추가

def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]            #스택
    visited = []                    #방문한 노드
    
    while stack:                    #스택이 아무것도 없을때 까지 돌아라  (아무것도 없으면 탈출)
        current_node = stack.pop()  # current_node라는 곳에 stack 마지막 부분을 빼서 넣기
        visited.append(current_node)     # 방문한 노드에 넣기(스택에서 꺼낸 것)
        for adjacent_node in adjacent_graph[current_node]:    # 인접한 노드들을 꺼내기          (current_node의 인접한 노드를 보기위해 뒤에 추가)
            if adjacent_node not in visited:    # 만약 인접한 노드가 visited에 없으면 방문 안한거니까 스택에 추가
                stack.append(adjacent_node)
    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!