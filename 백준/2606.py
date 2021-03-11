# 문제
# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

# 예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 
# 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 
# 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.



# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# 출력
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

# 예제 입력 1 
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
# 예제 출력 1 
# 4

n = int(input())    #컴퓨터의 총 수
m = int(input())    #컴퓨터끼리 연결되어 있는 수
graph = []
# graph_dic = {}
for i in range(1, m+1):      #컴퓨터끼리 연결되어 있는 수만큼 graph입력받기
    graph_plus = list(map(int,input().split()))
    graph.append(graph_plus)
    # graph_list = list(map(int,input().split()))
    
    # graph_dic[graph_list[0]] = graph_list
    

    
# print(graph)


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]            #스택
    visited = []                    #방문한 노드
    visite_num = 0
    while stack:                    #스택이 아무것도 없을때 까지 돌아라  (아무것도 없으면 탈출)
        current_node = stack.pop()  # current_node라는 곳에 stack 마지막 부분을 빼서 넣기
        visited.append(current_node)     # 방문한 노드에 넣기(스택에서 꺼낸 것)

        if visite_num < len(graph):
            for adjacent_node in adjacent_graph[visite_num]:    # 인접한 노드들을 꺼내기          (current_node의 인접한 노드를 보기위해 뒤에 추가)
                if adjacent_node not in visited:    # 만약 인접한 노드가 visited에 없으면 방문 안한거니까 스택에 추가
                    stack.append(adjacent_node)
            visite_num += 1
        else: 
            break
    return visited


print(dfs_stack(graph, 1)) 