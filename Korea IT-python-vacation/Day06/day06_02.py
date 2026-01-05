coords = [
    (3, -3),
    (2, 3),
    (1, -2),
    (5, 6)
]
my_coords = []
# 좌표들 중 1사분면에 해당하는 좌표만 모아주세요
for x,y in coords:
    if x>0 and y>0:
        my_coords.append((x,y))

print(my_coords)

# dict: key-value
scores = {
    "김철수": 90,
    "김영희": 80,
    "김민수": 100,
    "박철수": 50,
    "박영희": 45
}
# values들만 모아서 리스트로 가져다줄 수 있음
score_nums = scores.values()
print(score_nums)
# 평균점수 구하기
"""
score_sum = 0
for score in score_nums:
    score_sum += score # 누적합

score_avg = score_sum/len(score_nums)
print(score_avg)
"""
# 60점 이상 학생들의 평균점수
# len() x

score_sum = 0
count = 0
for score in score_nums:
    if score >=60:
        score_sum += score
        count += 1

print(score_sum/count)
"""
# 방법 2 새로운 리스트를 사용하여 len을 사용
score2 = []
score_sum2 = 0
for score in score_nums:
    if score >= 60:
        score2.append(score)
        score_sum2 += score

print(score_sum2/len(score2))

# scores에서 60점이상인 학생들의 이름을 출력해주세요
# dict -> {이름: 점수}
# items 사용하면 tuple로 나와짐
score_items = scores.items()
print(score_items)

for item in score_items:
    name , score = item # 튜플 언패킹
    if score >= 60:
        print(f"{name}님 합격입니다!")

"""
tele_book = {
    "김철수": "01011111111",
    "박철수": "01022222222",
    "최철수": "01033333333",
    "이철수": "01044444444",
}
target_number = input("찾으시는 전환번호를 - 빼고 입력 >>")
is_exist_number = False
# target_number가 dict에 value로 존재한다면, 이름을 출력 / 없다면 "발신자 알수없음"
for book in tele_book.items():
    name, number = book
    if number == target_number:
        print(name)
        is_exist_number = True
        break
# 반복을 다 돌았지면 ,여전히 False --> 없는전화번호
if not is_exist_number:
    print("발신자 알수없음")













