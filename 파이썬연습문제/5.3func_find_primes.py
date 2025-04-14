# 5.3 시작값, 끝값을 인자로 받아 그 사이의 소수를 리스트로 반환하는 find_primes 함수를 작성하세요.

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

start = 10
end = 50

print("소수 리스트:", find_primes(start, end))