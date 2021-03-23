n = int(input()) #집 
color = []

for i in range(n):
    a = list(map(int,input().split()))
    color.append(a)

for i in range(1, n):
    color[i][0] = min(color[i-1][1], color[i-1][2]) + color[i][0]
    color[i][1] = min(color[i-1][0], color[i-1][2]) + color[i][1]
    color[i][2] = min(color[i-1][0], color[i-1][1]) + color[i][2]

print(min(color[n-1]))
