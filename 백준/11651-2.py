# 좌표 정렬하기 2

# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# 예제 입력 1 
# 5
# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3
# 예제 출력 1 
# 1 -1
# 1 2
# 2 2
# 3 3
# 0 4

n = int(input())
in_list = []
for i in range(n):
    tt = list(map(int,input().split()))
    in_list.append(tt)


def selection_sort(in_list):
    n = len(in_list)
    for i in range(n-1):
        min_index = i               #최솟값을 위한 인덱스
        for j in range(n-i):
            if in_list[i+j][1] == in_list[min_index][1]:
                if in_list[i+j][0] > in_list[min_index][0]:
                    min_index = i+j
                in_list[i], in_list[min_index] = in_list[min_index], in_list[i]    
            elif in_list[i+j][1] < in_list[min_index][1]:
                    min_index = i+j
        in_list[i], in_list[min_index] = in_list[min_index], in_list[i]
        

selection_sort(in_list)

aa = in_list
print(aa) # [1, 2, 4, 6, 9] 가 되어야 합니다!