# 그룹 단어 체커


# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# 예제 입력 1 
# 3
# happy
# new
# year
# 예제 출력 1 
# 3
# 예제 입력 2 
# 4
# aba
# abab
# abcabc
# a
# 예제 출력 2 
# 1

n = int(input())

dap = 0
for i in range(n):
    count = 0
    word = list(input())
    
    if len(word) == 1:              #한글자인 경우
        count = 0
    
    for j in range(len(word)-1):            #끝글자는 비교할게 없으니 -1
        if word[j] != word[j+1]:       #뒤에 글자와 같지 않는다면
            new_word = word[j+1:]       # 새로운 단어 생성 = word[j] 글자를 뺀 단어
            if new_word.count(word[j]):         #새로운단어(그전에 비교한 글자를 뺀 것)에서 그전글자가 나온다면?카운팅된다면 
                count += 1                      # 카운트 올려줌
                break

    if count == 0:
        dap += 1

print(dap)