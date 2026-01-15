colors = ["빨강","파랑","노랑","블랙","화이트"]

# 아래의 코드에서 예외가 발생 경우의수를 고려하여 예외처리를 작성해주세요
# 정상적이면 result 출력, 언제나 "안녕히 가세요" 출력
# try:
#     my_idx = input("번호입력 >")
#     my_idx = int(my_idx)
#     result = colors[my_idx]
# except ValueError as e:
#     print("번호를 입력하세요")
# except IndexError as e:
#     print("올바른 인덱스를 입력하세요")
# else:
#     print(result)
# finally:
#     print("안녕히 가세요")


# raise: 예외를 의도적으로 생성하는 문법
try:
    raise ValueError("저는 님이 만든 에러입니다.")
except ValueError as e:
    # e의 메세지
    print(e)

# 커스텀(비즈니스)에러
# Exception을 상속받으면 된다.
# Exception - 모든 에러의 부모클래스
class NegativeScoreError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message

try:
    score = input("점수는 입력하세요!")
    score = int(score)
    if score < 0:
        raise NegativeScoreError("점수는 음수일수 없습니다")
except NegativeScoreError as e:
    print(e)

# 커스텀에러를 정의하고 사용자에게 이메일 주소를 입력받고, @, .com가 없으면 InvalidEmailError 예외를 발생
# 올바르다면 -> 올바른 이메일형식입니다 출력!
# 올바르지 않다면 -> 에러메시지 출력! (에러메세지: 유효하지 않은 이메일형식)

class InvalidEmailError(Exception):
    def __init__(self):
        self.message = "유효하지 않은 이메일 형식"
        super().__init__(self.message)

try:
    email = input("email을 입력하세요:")
    if "@" not in email or not email.endswith(".com"):
        raise InvalidEmailError()
except InvalidEmailError as e:
    print(e)
else:
    print("올바른 이메일 형식입니다")

"""
시스템이 복잡해지면 리턴->리턴->리턴-> ........ 복잡도 상승
return으로는 한계가 있음
즉시 멈추고 바로 탈출할 수 있는 문법이 필요하다! -> 커스텀예외 던지기
"""