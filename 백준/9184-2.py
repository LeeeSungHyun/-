
# if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
#     1

# if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
#     w(20, 20, 20)

# if a < b and b < c, then w(a, b, c) returns:
#     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

# otherwise it returns:
#     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

def w(a, b, c):
    if (a, b, c) in memo.keys():
        return memo[(a,b,c)]
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        memo[(20,20,20)] = w(20,20,20)
        return memo[(20,20,20)]

    elif a<b<c :
        memo[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[(a,b,c)]

    else:
        memo[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[(a,b,c)]

memo = {}

while True:
    a, b, c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print('w(%d, %d, %d) = %d'%(a, b, c, w(a,b,c)))


