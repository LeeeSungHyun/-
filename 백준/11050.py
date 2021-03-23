# 이항계수

# 문제
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 
# 를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤  ≤ 10, 0 ≤  ≤ )

# 출력
 
# 이항계수를 출력한다.

# 예제 입력 1 
# 5 2
# 예제 출력 1 
# 10

# n! / (k!(n-k)!)
memo = {
    1: 1,
    2: 2
}
def factory(num):                             #팩토리얼 구하는 함수
    if num <= 1:                    ######  ==1로 하면 런타임에러, <=1로 해줘야 함
        return 1
        
    if num in memo:                             # 메모에 있으면 그대로 불러오기
        return memo[num]
                              
    fac = num * factory(num-1)
    memo[num] = fac              # 메모에 저장
    return memo[num]                 



n, k = map(int,input().split())
nn = n-k                                
nf = factory(n)                
kf = factory(k)
nnf = factory(nn)
dap = nf // (kf * nnf)                      # 이항계수의 공식 n! / (k!(n-k)!)      if 0<= K <= N 일때

print(dap)

