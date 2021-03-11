

## 접근 방식
# 알파벳과 발생횟수를 key:value형태로 저장한 뒤 value값을 기준으로 내림차순 정렬한다.
# 정렬된 배열에서 발생횟수가 동일한 알파벳이 있는 지 확인하여 있다면 물음표를, 없다면 알파벳 대문자를 출력한다.



word = str(input()).upper()

count = {}

for char in word:
    if char in count:
        count[char] += 1
    else :
        count[char] = 1

sorted_count = sorted(count.items(), key = lambda x:x[1], reverse =True)    #람다식
#Tuple 형태여서 value로 가져올 수 없으므로 인덱스를 주어 발생횟수를 가져온다.

if len(sorted_count) > 1 :
    if sorted_count[0][1] == sorted_count[1][1]:
        print('?')
    else :
        print(sorted_count[0][0])
else :
    print(sorted_count[0][0])