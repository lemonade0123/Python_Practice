# 10000원을 3명이서 똑같이 나누어 가질 때 각자 얼마를 받고 얼마가 남는지 계산하세요.

total_money = 10000
num_people = 3

each = total_money // num_people
remainder = total_money % num_people

print(f"각자 {each}원을 받고 {remainder}원이 남습니다")