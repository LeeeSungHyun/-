# 문제
# 재귀 호출만 생각하면 신이 난다! 아닌가요?

# 다음과 같은 재귀함수 w(a, b, c)가 있다.

# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1

# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)

# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
# 위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

# a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다. 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

# 출력
# 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

# 제한
# -50 ≤ a, b, c ≤ 50
# 예제 입력 1 
# 1 1 1
# 2 2 2
# 10 4 6
# 50 50 50
# -1 7 18
# -1 -1 -1
# 예제 출력 1 
# w(1, 1, 1) = 2
# w(2, 2, 2) = 4
# w(10, 4, 6) = 523
# w(50, 50, 50) = 1048576
# w(-1, 7, 18) = 1

###### 딕셔너리로 메모공간 저장하고 키값을 abc 각각 문자열로.. 해보기


def num_list(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return num_list(20, 20, 20)                         # [a][b][c] 중 하나라도 20이 넘으면 모든값 20!

    if dp[a][b][c] :                                        # 3차원 배열 안에 abc값이 있다면
        return dp[a][b][c]                                  # 그 값 가져오기

    if a<b<c :                                                                              #예시로 주어진 조건
        dp[a][b][c] = num_list(a,b,c-1) + num_list(a,b-1,c-1) - num_list(a,b-1,c)           
    else:
        dp[a][b][c] = num_list(a-1,b,c) + num_list(a-1,b-1,c) + num_list(a-1,b,c-1) - num_list(a-1,b-1,c-1)

    return dp[a][b][c]



dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]             # 3차원 배열 만들기 0부터 20까지인 -> 위에 조건중 하나라도 20이 넘으면 값이 20이기 때문에?

                        

while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print('w(%d, %d, %d) = %d' %(a, b, c, num_list(a,b,c)))



