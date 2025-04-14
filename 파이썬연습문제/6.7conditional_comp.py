# 6.7 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 짝수는 제곱, 홀수는 그대로인 새 리스트를 생성하세요.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [num ** 2 if num % 2 == 0 else num for num in numbers]

print(result)
