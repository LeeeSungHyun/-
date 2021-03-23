# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

# 예제 입력 1 
# 3 1
# 예제 출력 1 
# 1
# 2
# 3

N, M = map(int, input().split())                # M = 수열의 길이

num_list = [i + 1 for i in range(N)]            # 1부터 n까지의 숫자가 각각 담긴 리스트 생성
check_list = [False] * N                        # n까지의 길이만큼 리스트 생성 하고 그 안에 값을 모두 False로 설정

arr = []                                # 출력할 수열을 담을 리스트

def dfs(cnt):                           
    if(cnt == M):                       # 수열의 길이와 arr[]크기가 같으면 출력
        print(*arr)                         
        return
    
    for i in range(0, N):              
        if(check_list[i]):              # check_list[i] 값이 True 면 continue 실행 후 다음 for문 값 받음
            continue
        
        check_list[i] = True            # True 값 반영
        arr.append(num_list[i])         # 수열담을 리스트에 값 넣기
        dfs(cnt + 1)                    # 재귀함수로 (그다음자리) 수열 값 찾기 
        arr.pop()                       # 수열이 출력되고 난 뒤 맨 뒤에 값 빼기
        
        # 이 부분이 순열하고의 차이점이다.
        # 큰 나무에서 전에 봤던 것만
        # 닫아주면 된다.
        for j in range(i + 1, N):               
            check_list[j] = False               # ex) 1부터 이어진 수열 끝나면 1은 True 고정 -> 2부터 검사 하게끔..
            
        
dfs(0)