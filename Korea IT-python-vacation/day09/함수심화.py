# 매개변수의 기본값 설정
def hello(name, nationality="대한민국"):
    print(f"{name} {nationality}")
hello("홍길동") # 기본값 사용
hello("김길동", "미국")

# 기본값 설정이 안되어있는 매개변수는
# 기본값 설정이 되어있는 매개변수 뒤에 올 수 없다.
#def hello(nationality="대한민국",name):
#    print(f"{name} {nationality}")
#print("홍길동") --->오류를 발생
# 이유: 파이썬은 매개변수를 들어오는 데이터의 순서로 기억
# 기본값설정이 되어있는게 나중 순서로 와야 명확하게 데이터를 할당가능

# *args 패킹
# 여러개로 들어온 매개변수들을 tuple에 담아서 하나로 가져온다
print("어쩌고", "저쪼고", "이러쿵", "저러쿵")
# 매개변수명이  *args가 아님 매개변수명은 args "*"은 튜플로 가져온다 라는 의미임
def args_fx(*args):
    # 매개변수의 갯수와 무관하게 모두 tuple 하나로
    # 포장해서 들어온다.
    print(type(args))
    print(args)

args_fx(1,2,3)

def calc_sum(*numbers):
    numbers_sum = 0
    for num in numbers:
        numbers_sum += num
    return numbers_sum
print(calc_sum(1,2,3,4,5,6))

# 권장) *args 패킹을 쓸때는 가장 뒷쪽 매개변수로 설계하자

# **kwarg 패킹
# 여러값을 하나의 dict로 묶어서 전달
# 매개변수 이름이 **details가 아님
# 매개변수 이름은 details임
def make_user(name, **details):
    print(type(details))
    user = {
        "name": name,
    }
    user.update(details)
    return user
# key = "데이터"
result = make_user("홍길동", age=20, hobby="축구")
print(result)

# **kwargs 언패킹

def print_user(**user):
    print(user)

print_user(name="홍길동", age=20) # kwargs 패킹
other_data = {
    "name": "김길동",
    "age": 20,
    "address": "부산"
}
# * kwargs 언패킹
# 이미 dict로 포장되어있으니, 또 포장하지마세요
print_user(**other_data)