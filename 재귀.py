# def count_down(number):
#     if number >= 0:        
#         print(number)          # number를 출력하고
#         count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!

# count_down(60)


# Factorial(N) = N * factorial(N-1)
#팩토리얼 구하기

# def factorial(n):
#     # 이 부분을 채워보세요!
#     if n==1:
#         return 1

#     return n* factorial(n-1)


# print(factorial(5))


#회문검사
# input = "abcba"


# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n-1-i]:
#             return False
#     return True


# print(is_palindrome(input))


#회문검사 재귀함수 이용
# input = "abcba"


# def is_palindrome(string):
#     if string[0] != string[-1]:
#         return False
#     if len(string) <= 1:
#         return True
#     return is_palindrome(string[1:-1])


# print(is_palindrome(input))


# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n-1-i]:
#             return False
#     return True
    

# print(is_palindrome('토마터토'))


# def is_palindrome(string):
#     if string[0] != string[-1]:
#         return False
#     if len(string) <= 1:
#         return True
#     return is_palindrome(string[1:-1])

# print(is_palindrome('토마미미마토'))



numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    return 5


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!