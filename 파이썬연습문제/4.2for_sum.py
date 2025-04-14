# 4.2 1부터 100까지의 숫자 중 3의 배수의 합을 구하세요.

sum_of_multiples = 0
for i in range(3, 101, 3):
    sum_of_multiples += i

print("3의 배수의 합:", sum_of_multiples)
