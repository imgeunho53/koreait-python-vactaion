# day01_02.py

#str의 기능들
my_str = "hello, world!"

#문자열의 길이 - len(문자열데이터)
my_str_length = len(my_str)
print(my_str_length) # 13

# 문자열 슬라이싱
# 문자열 데이터[시작번호 : 끝번호]
#시작번호 이상 ~ 끝번호 미만
print(my_str[0:5])
print(my_str[:5]) # 0은 생략가능
print(my_str[7:]) # 뒤를 생략하면 끝까지라는 의미

# 실습) ssn에 담긴 주민번호의 뒷자리를 "*" 로 바꾸어주세요
#991111-1234567 -> 991111-******* 출력!
ssn = "991111-1234567"

print(ssn[:7] + "*" *7)

# find() : 해당 문지의 위치 (index) 가져온다
# 만약에 해당문자가 없으면 -1을 가져옴
# index() : 해당문자의 위치 (index)를 가져온다
# 만약에 해당문자가 없으면 에러를 일으킨다

index_of_dash = ssn.index("-")

#뒷자리 문자개수
length_last_ssn = len(ssn[index_of_dash + 1:])

# 문자열의 곱셈 가능
print(ssn[:7] + "*" * length_last_ssn)

#주민번호 앞지리
first_ssn = ssn[: index_of_dash + 1]

print(first_ssn + "*" * length_last_ssn)
# data가 어떻게 변할 지 모르기 때문에 변수를 사용하는 것이 효율적

# 실습) 이메일 데이터에서 id만 추출
# 조건) 데이터가 바뀌더라도 , id가 추출되어야 합니다.
email = "super_python@py.com"

at_index = email.find("@")
username = email[: at_index]

print(username)

## day01 : 입출력, 문자열 기능






