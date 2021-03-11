# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}
# 1. 시작노드를 큐에 넣기
# 2. 현재 큐의 노드를 빼서 visited에 추가(맨앞에꺼)
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가

def bfs_queue(adj_graph, start_node):
    visited = []    #방문한 노드
    queue = [start_node]      #큐
    # queue.append(start_node)
    
    while queue:        #스택이 아무것도 없을 때 까지 돌아라
        current_node = queue.pop(0)             #current_node = 방문한 노드
        visited.append(current_node)
        
        for adj_node in adj_graph[current_node]:  #adj_node = 인접한노드 
            if adj_node not in visited:
                queue.append(adj_node)

    
    return  visited             #visited 반환


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!