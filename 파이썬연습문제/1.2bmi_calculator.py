# 1.2 사용자로부터 체중(kg)과 키(cm)를 입력받아 BMI를 계산하세요.

weight = float(input("체중(kg): "))
height_cm = float(input("키(cm): "))

height_m = height_cm / 100

bmi = weight / (height_m ** 2)

print("BMI:", round(bmi, 1))
