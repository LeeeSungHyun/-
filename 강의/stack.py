top_heights = [6, 9, 5, 7, 4]

#[0, 0, 2, 2, 4]
#[0, 0, 0, 0, 0]   으로 만들고 맨 오른쪽부터 탐색
# <- <- <- <- <- 왼쪽으로 레이저
#           7  4

#[0, 0, 0, 0, 4]

#[6, 9, 5, 7, 4]
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)         #[0, 0, 0, 0, 0]
    while heights:                  #heights가 빈상태가 아닐 때 까지 반복 빈상태면 탈출
        height = heights.pop()                # 마지막 데이터 뽑음 (첫번째는 4)
        for idx in range(len(heights)-1, 0,-1):     # 위에서 데이터 뽑아서 len(heights)는 4
            if heights[idx] > height:       #heights의 현재 인덱스 값이 가장위에서 뽑은 데이터보다 크다면?   -- heights[3] = 7 > 4  레이저가 박힌다면?
                answer[len(heights)] = idx + 1      
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
