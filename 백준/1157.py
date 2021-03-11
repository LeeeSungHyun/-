# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 예제 입력 1 
# Mississipi
# 예제 출력 1 
# ?
# 예제 입력 2 
# zZa
# 예제 출력 2 
# Z
# 예제 입력 3 
# z
# 예제 출력 3 
# Z
# 예제 입력 4 
# baaa
# 예제 출력 4 
# A

A = str(input().upper())  # 대문자로 문자열 변경 
A_list = list(set(A))     # 리스트 안에 set함수로 중복알파벳 제거
cnt = []                  # 비어있는 리스트 생성

for i in A_list:              # 중복알파벳 제거 된 리스트로 for문
    count = A.count(i)        # A_list 안에 있는 알파벳을 A로 입력한 단어에서 몇개인지 count 
    cnt.append(count)         # count 된 값을 cnt 리스트에 넣기

if cnt.count(max(cnt)) >= 2:     # count 된 값이 있는 cnt리스트에서 제일 높은 숫자가 2개 이상일 경우
    print("?")                  
else:   
    print(A_list[(cnt.index(max(cnt)))])           # ex)  A=bbap, A_list = ['B', 'A', 'P'], cnt = ['2', '1', '1']
                                                   # 여기서 max(cnt) = 2  index(2)는 cnt에서 cnt[0]에 위치 --> A_list[0] = B

                                                   # ex) A=dkDp, A_list = ['K', 'D', 'P'], cnt = ['1', '2', '1']
                                                   # max(cnt) = 2, index(2) cnt[1] --> A_list[1] = D
    
    

    