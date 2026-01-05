# 이중 for문 - 비교
s1 = ["a","b","c"]
s2 = ["com", "b", "d", "p", "c"]
# s1과 s2 배열의 유사도를 출력 - 같은 요소가 몇개?

count = 0
for x in s1:
    for y in s2:
        if x == y:
            print(f"{x}와 동일한데이터 {y}발견")
            count += 1

print(count)

# break & continue
# break를 읽으면 반복문을 한번 탈출
for num in range(10):
    # 10번반복 중 num이 5가 되면 탈출
    if num == 5:
        print("5가 되었습니다. 탈출!")
        break
    else:
        print(num)
# continue를 읽으면 다음반복을 즉시 실행
for num in range(10):
    # 10번반복 중 num이 5가 다음반복 실행
    if num == 5:
        print("5가 되었습니다. 스킵!")
        continue
    else:
        print(num) # num이 5면 실행되지 않음


# 짝수만 출력!
for num in range(10):
    if num %2 !=0: # 홀수면
        continue # 다음반복

    print(num)

foods = ["계란", "우유(상함)",
         "사과", "김치", "수박(상함)"]

# "(상한)" 이 포함되지 않은 음식만 출력!
# in 연산자
for food in foods:
    if "(상함)" in food:
        continue
    else:
        print(food)

for food in foods:
    # food는 대입받는 변수이지 원본x
    if "(상함)" in food:
        food = food[:-4] # 대입받는 변수를 수정한것

print(foods)

# 원본을 수정하려면? 인덱스정보가 필요하다
# enumerate(): 리스트 데이터를 (인덱스, 데이터) 튜플형태로 만들어준다
# ["계란", "우유(상함)","사과", "김치", "수박(상함)"]
# [(0, "계란"). -------------(4, "수박(상함)")]

samples = enumerate(foods)
# idx, food = (0, "계란")
for idx, food  in samples: # 튜플언패킹
    print(f" {idx}: {food}")

for idx, food in enumerate(foods):
    # "(상함)"
    if "(상함)" in food:
        # 원본 수정
        foods[idx] = food[:-4]

print(foods)

fruits = ["사과", "바나나", "체리", "포도", "망고"]
# 홀수 인덱스에 있는 것만 출력해 주세요!
# continue 사용 enumerate() 사용
for idx, fruit in enumerate(fruits):
    if idx % 2 == 0:
        continue

    print(fruit)

















