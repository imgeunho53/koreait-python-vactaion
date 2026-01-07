"""
변수? 데이터 재사용
함수? 코드를 재사용

함수정의
def 함수이름(매개변수1, 매개변수2.....):
    코드 작성

    return 데이터

- 매개변수와 리턴은 선택사항
- 헷갈리는 부분 정리
함수 정의와 함수 호촐을 헷갈리지 말자!
"""
# 매개변수 x, 리턴x
def hello():
    # 호출되면 아래의 코드를 실행하세요
    print("안녕하세요!")
    print("반갑습니다!")
# 함수호출 - > 함수가 가지고있던 코드가 실제 실행
hello()

his_name = "최길동"
# 매개변수 o, 리턴x
def hello_name(name):
    # 매개변수: 함수가 호출될 때 외부에서 전달받는 값을 저장
    # 생존범위가 존재한다
    # 함수 안에서만 유효 ex) print(name) 이런거 안됨
    print(f"{name}님 안녕하세요!")
    print(f"{name}님 반갑습니다!")
    # print(f"{his_name}님 안녕하세요") 일반변수는 함수 내에서 사용가능
hello_name("홍길동")
hello_name("박길동")
my_name = "박화목"
hello_name(my_name)
"""
# introduce라는 함수
# 이름과 나이를 전달받아서,
# 안녕하세요. 저는 ~이고, ~살입니다.
def introduce(name, age):
    print(f"안녕하세요 저는 {name}이고 {age}살 입니다")
name = input("이름을 입력하세요:")
age = input("나이를 입력하세요:")
introduce(name,age)
"""
# 매개변수 x 리턴 o
def get_100():
    print("get_100 호출되었습니다!")
    return 100 # return을 읽으면 함수가 즉시종료

return_value = get_100()
print(f"리턴받은값: {return_value}")

# 매개변수 o 리턴 o
def add(x, y):
    sum = x + y
    return sum

# 호출결과가 값이면 값, 특별한 자료형데이터라면 그 데이터처럼 다룰 수 있다
result = add(10, 20)
print(result)
# f(g()) -> g()호출/실행 ->f()호출/실행
result2 = add(add(10,20),add(10,20))
print(result2)
score_list1 = [55, 70, 100]
score_list2 = [60,70,100]
score_list3 = [70,80,90]
def calcAvg(score_list):
    sum = 0
    for score in score_list:
        sum += score
    avg = sum / len(score_list)
    return avg
print(calcAvg(score_list1))
print(calcAvg(score_list2))
print(calcAvg(score_list3))

# 주민등록번호를 매개변수로 전달받아서
# "991122-1122334"
# "-" 빼고 13자리인지?
# 숫자인지?
# 모두 충족되면 True를 리턴, 하나라도 안되면 False 리턴
pn = "991122-1122334"
def validate_pn(pn):
    # "991122-1122334"
    pn = pn.replace("-","")
    # "9911221122334"
    if  pn.isdecimal() and len(pn) == 13:   # if not len(pn) ==13: return False, if not pn.isdecimal(): return False
        return True # 얼리 리턴   # 월 검사 month = pn[2:4] if not (1<= month <= 12), month = int(month): return False , day도 마찬가지

    return False
    # 1,3이면 "남자" 리턴
    # 2,4이면 "여자" 리턴
    # 그외는 "외국인" 리턴
# 주민번호를 받아서 남자인지 여자인지 리턴
def get_gender(pn):
    if not validate_pn(pn):
        return "유효하지 않은 주민번호입니다."
    gender_digit = pn[7]
    gender_digit = int(gender_digit)
    if gender_digit in [1,3]:
        return "남자"
    elif gender_digit in [2,4]:
        return "여자"
    else:
        return "외국인"
print(get_gender(pn))

# print() 매개변수 갯수가 변한다.
print("안녕하세요", "반갑습니다")
# 입력한데이터 끝에 엔터가 자동추가?
print("안녕하세요", end="")


# 매개변수에 기본값을 지정할 수 있다.
def print_info(name, age ,nationality = "대한민국"): # 기본값 설정 / 굳이 매개변수를 입력하지않아도 대한민국으로 출력됨
    print(f"이름: {name}, 나이:{age}, 국적:{nationality}")

















