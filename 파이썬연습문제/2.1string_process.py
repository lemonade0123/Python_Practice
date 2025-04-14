# 2.1 "Hello"와 "World"를 연결하여 "Hello World"를 출력하세요.대문자로 변환하세요 "Hello World"에서 "World"만 슬라이싱하여 출력하세요.

greeting = "Hello"
target = "World"
combined = greeting + " " + target
print(combined)

print(combined.upper())

print(combined[6:])

text = "Python is fun"
print(text.split())

letters = "abcdef"
print(letters[::2])

print(greeting * 3)