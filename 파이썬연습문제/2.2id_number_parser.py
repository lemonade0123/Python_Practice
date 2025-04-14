# 2.2 주민등록번호 "901212-1234567"에서 생년월일을 추출하세요. 

id_number = "901212-1234567"

yy = id_number[0:2]
mm = id_number[2:4]
dd = id_number[4:6]
century_code = id_number[7]

if century_code in ['1', '2']:
    year = "19" + yy
elif century_code in ['3', '4']:
    year = "20" + yy
else:
    year = "??" + yy  

print(f"{year}년 {mm}월 {dd}일")
