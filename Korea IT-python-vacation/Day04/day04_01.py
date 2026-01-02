# 튜플(tuple)
# 변경이 불가능한 리스트
# 한번 데이터가 들어오면 "불변"(원본훼손 x)

numbers = (1,2,3,4)
number = (1,) # 요소가 하나일때는 쉼표
fruits = ("사과", "바나나", "포도", "수박")

print(fruits[0]) # 인덱싱으로 조회가능
# fruits[0] = "망고"

# idx를 찾을 수 있음
# 0번부터 조회해서 처음발견된 idx만 가져옴
grape_idx = fruits.index("포도")  # 중복값은 무시
print(grape_idx)

# 갯수찾기
grape_count = fruits.count("포도")
print(grape_count)

# 슬라이싱은 가능
# 슬라이싱은 원본은 건드리지 않고
# 복사해서 가공하여 새로 만들어주는 것
names = ("홍길동", "김길동", "박길동")
print(names[:2]) #슬라이싱
print(names) # 원본은 보존 됨

# 리스트는 불변? --->X
sample = ["데이터1", "데이터2", "데이터3"]
print(sample)
sample.append("데이터4")
print(sample)

# 튜플 언패킹
mr_kim = ("김길동", "대한민국", 30 , "남자")
name, nationality, age, gender = mr_kim
print(name, nationality, age, gender) # 대입확인

# 값 바꾸기
a = 10
b = 20

a ,b = b, a
print(a, b)

# 실습) 주어진 coord좌표가 몇사분면에 있는지 판별해서 출력
coord = (3, -3)
a, b = coord
if a>0 and b>0:
    print("1사분면입니다")
elif a<0 and b>0:
    print("2사분면입니다")
elif a>0 and b<0:
    print("4사분면입니다")
else:
    print("3사분면입니다")
# if조건문은 하나씩 하나씩 검사 elif는 위에서 아래로 검사


#컬렉션자료형들(list , tuple, set)
#서로 형변환이 가능
example = ("데이터1", "데이터2")
list_example = list(example)
print(list_example) # 리스트로 변환
tuple_example = tuple(list_example) # 튜플로 변환




























































