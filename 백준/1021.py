# 문제
# 지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

# 지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

# 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
# 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.

# 큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. 
# (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 
# 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# 예제 입력 1 
# 10 3
# 1 2 3
# 예제 출력 1 
# 0
# 예제 입력 2 
# 10 3
# 2 9 5
# 예제 출력 2 
# 8
# 예제 입력 3 
# 32 6
# 27 16 30 11 6 23
# 예제 출력 3 
# 59
# 예제 입력 4 
# 10 10
# 1 6 3 2 7 9 8 4 10 5
# 예제 출력 4 
# 14


# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# idxs = list(map(int, input().split()))
# dq = deque([i for i in range(1, n+1)])

# count = 0
# for idx in idxs:
#     while True:
#         if dq[0] == idx:
#             dq.popleft()
#             break
#         else:
#             if dq.index(idx) < len(dq)/2:
#                 while dq[0] != idx:
#                     dq.append(dq.popleft())
#                     count += 1
#             else:
#                 while dq[0] != idx:
#                     dq.appendleft(dq.pop())
#                     count += 1
# print(count)


# 1. 큐 중에서도 양쪽으로 삽입삭제가 가능한 덱(deque)을 사용했다.

# 2. 인덱스(1부터)만 주어지고, 각 인덱스의 값은 몰라도 되므로, 편하게 계산하기 위해 각 인덱스를 값으로 가지는 큐 dq를 만들어 사용했다.

# 3. 입력받은 인덱스를 저장한 배열 idxs를 탐색한다.

# 4. idxs의 원소 idx가 큐에서 제거될 때까지 반복한다.

#   4-1. dq의 맨 앞 원소가 현재 idx와 같다면, 제거 후 break

#   4-2. 같지 않다면, dq에서의 idx의 위치를 알아낸다.

#     4-2-1. 위치가 dq의 앞쪽이라면, 앞 원소를 빼서 뒤로 보내는것이 빠르므로, idx가 dq의 맨 앞으로 올 때까지 문제의 2번 연산 수행 후 count 1 증가

#     4-2-2. 위치가 dq의 뒤쪽이라면, 뒤 원소를 빼서 앞으로 보내는것이 빠르므로, idx가 dq의 맨 앞으로 올 때까지 문제의 3번 연산 수행 후 count 1 증가

#     4-2-3. 여기서 신경써야 할 점은, dq의 길이가 홀수일 때는 중간 인덱스까지 앞으로 돌리는 것이 빠르므로, (dq의 길이/2)값이 자동 내림되지 않도록 해야한다. 
#    (1 2 3 4 5 일때, 1 2 3은 앞으로, 4 5는 뒤로)

#   파이썬에서는 자동으로 double값의 결과가 나오지만, 자바에서는 int나눗셈은 결과의 소수점을 다 버리고 int 로 변환되므로, 
#   ((double)dq의 길이/2)로 바꾸어 비교해야한다.
n, m = map(int,input().split())         # n = 큐의 크기  m = 뽑아내려는 수의 개수
wantnum = []                            # 1부터 n까지 값을 담을 리스트
search = []                             # 원하는 수 찾으면 담아놓기
t = list(map(int,input().split()))      #찾으려는 수 

count = 0                               #2번, 3번 사용한 횟수를 위한 count

for i in range(1, n+1):
    wantnum.append(i)                               #1부터 n까지의 리스트 생성하기


while len(t) != len(search):                    #내가 찾을 숫자들의 개수와 그것들을 찾은 개수가 같아지면 반복문 탈출!
    for i in range(0, len(t)):
        tlength = len(wantnum) // 2                        #위치 비교를 위해 wantnum 길이의 반 정의
        
        if wantnum[0] == t[i]:                                 #1번
            search.append(t[i])                                #반복문 탈출위해 search리스트에 찾은거 넣어놓기
            wantnum.pop(0)
        elif tlength >= wantnum.index(t[i]):                   # wantnum 리스트 길이의 가운데랑 t[i]값으로 wantnum안에 위치를 비교하기?
            while wantnum[0] != t[i]:                          # 맨앞이 일치하면 반복문 탈출
                wantnum.append(wantnum[0])                     # 2번 방법 맨뒤에 추가(맨앞에값) 한 후 맨 앞에 값 지우기
                wantnum.pop(0)      
                count += 1                                      #횟수 +1
            if wantnum[0] == t[i]:                             # 비교후 1번동작
                search.append(t[i])
                wantnum.pop(0)
        else:
            while wantnum[0] != t[i]:                           # 3번동작
                wantnum.insert(0, wantnum[-1])                  # 맨앞에(맨뒤에값) 추가 후 맨 뒤에 값 지우기
                wantnum.pop()
                count += 1
            if wantnum[0] == t[i]:                              #비교 후 1번동작
                search.append(t[i]) 
                wantnum.pop(0)    

print(count)

