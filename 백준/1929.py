# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 예제 입력 1 
# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13


import math

t, n = map(int,input().split())
array = [True for i in range(n+1)]  # n까지 모든 수가 소수다 (true) 설정

for i in range(2, int(math.sqrt(n)+1)):     #math.sqrt = 제곱근 루트 = n**0.5
    if array[i] == True:            

        j = 2           #j 초기값
        while i*j <= n:
            array[i*j] = False
            j += 1

for i in range(t, n+1):
    if array[i] and i!=1:           # 1은 소수가 아니므로 제외
        print(i)