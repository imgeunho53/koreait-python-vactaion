# [], {} 조작하는 문법
# [], {} 생성 / for / if 한줄 선언 문법

# 1. [] 컴프리헨션
nums = [1, 2, 3, 4, 5]
nums_square = []
for num in nums:
    nums_square.append(num**2)
# [연산식 for 변수 in 리스트 (if 조건 - 필터링)]
com_square = [num**2 for num in nums]

# 짝수들만 제곱
# 데이터의 일부분 조작
even_squares = [num ** 2 for num in nums if num % 2 == 0]
print(even_squares)

# 홀수는 그대로 두고, 짝수만 제곱
# 데이터 전체 조작 - [연산식(상항연산자) for 변수 in 리스트]
# True값 if 조건 else False값
even_squares = [num**2 if num % 2 ==0 else num for num in nums ]
print(even_squares)

# 전체데이터 예시
scores = [85, 42, 90, 55, 78] # 60점 커트라인
# [합, 불합 ,합 ,불합 ,합]
scores_cutline = ["합" if score >= 60 else "불합" for score in scores]
print(scores_cutline)

# 2. {} 컴프리헨션
"""
{ 
    1 : 1
    2 : 4
    3 : 9
    4 : 16
    5 : 25
}
"""
# {key: value for 변수 in 리스트}
square_dict = {num: num**2 for num in range(1,6)}
# 예시
fruits = ["apple", "banana", "cherry", "kiwi"]
# -> {"apple" : 5, "banana": 6}
result = {f: len(f) for f in fruits}
print(result)

# {} 컴프리헨션 -  조건문(필터링)
scores = {
    "철수" : 85,
    "영희" : 42,
    "민수" : 90,
    "지우" : 80
}
# {"파이썬고 - 이름": 점수} 60이상만
passing = {f"파이썬고 - {name}": score for name, score in scores.items() if score >=60 } # 필터링
print(passing)

origin = {"a": 1, "b": 2, "c": 3 }
# {1: "a", .... 3: "b"}
change = {v : k for k, v in origin.items()}
print(change)



menus = {
    "사과" : 2000,
    "바나나" : 1500,
    "귤" : 800
}
# menus에 있는 가격들을 * 0.9해서 10%할인시킨
# 결과 출력! {"사과" :1800, ....... "귤": 720}
menus_discount = {menu: int(price * 0.9) for menu, price in menus.items()}
print(menus_discount)

class Student:
    def __init__(self, st_id, st_name):
        self.st_id = st_id
        self.st_name = st_name
        # 다른 자료형에 담겨있을때 출력값
    def __repr__(self):
        return f"{self.st_id} : {self.st_name}"

st1 = Student(1, "김철수")
st2 = Student(2, "김철수")
st3 = Student(3, "김철수")
students = [st1, st2, st3]
print(students)

# 20260001, 20260002, 20260003 ......
# [] 컴프리헨션
# 객체정보 변환시, 생성자로 새로 만들어서 변경
prefix_students = [Student(f"2026000{st.st_id}",st.st_name) for st in students]
print(prefix_students)




















