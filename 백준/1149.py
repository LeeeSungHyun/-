# 문제
# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 
# 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 
# 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

# 예제 입력 1 
# 3
# 26 40 83
# 49 60 57
# 13 89 99
# 예제 출력 1 
# 96


### 이거는 그냥 각 집마다 최솟값구하는 거만 해당 -> 전체 집의 최솟값은 반례가 나옴

# n = int(input())            # 집의 갯수

# color = []

# result = []


# for i in range(0, n):
#     a = list(map(int,input().split()))
#     color.append(a)                             # i=0  [26,69,70]  , i=1 [1000,436,346]


#     if i == 0:
#         result.append(min(color[i]))
    
#     elif color[i].index(min(color[i])) == color[i-1].index(min(color[i-1])):
#             color[i][color[i].index(min(color[i]))] = 1000
#             result.append(min(color[i]))
    
#     else:
#         result.append(min(color[i]))

# dap = 0
# for i in result:
#     dap += i

# print(dap)
    

    
n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1, n):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1]))


