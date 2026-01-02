# set(셋) {}
# 순서가 없음 인덱싱이 안됌, 중복허용안됌
fruits = {"사과", "바나나", "딸기", "사과"}
print(fruits) # 중복값은 하나의 값으로 취급

# 요소추가
fruits.add("메론")
print(fruits)
fruits.update({"체리", "수박"})
print(fruits)

# 요소삭제
pop_fruits = fruits.pop() # 아무거나 꺼내옴
print(pop_fruits)
fruits.discard("체리") # 요소가 없어도 아무일 없음
fruits.remove("수박") # 요소가 없으면 에러발생

# 집합연산
a = {1,2,3,4,5}
b = {4,5,6,7,8}

# 합집합 : 합친뒤 중복값 제거
print(a | b)
print(a.union(b))

# 교집합 : 중복값만 추출
print(a & b)
print(a.intersection(b))

# 차집합 : 기존값에서 중복값 제거
print(a-b)
print(a.difference(b))

my_data = ["김밥", "우동", "마라탕", "탕수육", "김밥"]
set_data = set(my_data)
print(set_data) # 중복제거용, 다만 index가 꼬여버림
print(list(set_data))

# 실습
math_class = ["철수", "영희", "영수", "상호"]
eng_class = ["철수", "찬호", "영희", "동숙"]
# 둘다 출석한 학생 출력
# 수학만 출석한 학생 출력
math_class = set(math_class)
eng_class = set(eng_class)
print(math_class.union(eng_class))
print(math_class.difference(eng_class))

# 맞팔한 친구들의 이름들 출력!
following = { "민수": True, "철수": True,
              "지우": True, "나연": True}
follower = {"정우", "민수", "나연"}
# dict를 다른 컬렉션으로 변환시 key들만 추출되서 변환됨
following = following.keys()
following = set(following)
print(following.intersection(follower))

# 기출
a = {"한국", "중국", "일본"}
a.add("베트남")
a.add("중국")
a.remove("일본")
a.update({"홍콩", "한국", "태국"})
print(a)





