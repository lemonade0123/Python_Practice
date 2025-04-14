# 4.3 [70, 85, 90, 55, 78] 리스트에서 합격(60점 이상)한 점수만 출력하세요.

scores = [70, 85, 90, 55, 78]

for score in scores:
    if score >= 60:
        print(f"합격: {score}")
