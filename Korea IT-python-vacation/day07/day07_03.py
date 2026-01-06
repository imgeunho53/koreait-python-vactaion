import random

# 미니 로또
# 6개 중복없는 랜덤숫자
# 6:1등, 5:2등, 4:3등, 꽝

# 1. 당첨번호 뽑기
winning_nums = []
while True:
    random_num = random.randint(1,45)
    if random_num in winning_nums:
        continue
    winning_nums.append(random_num)
    # 6개 뽑으면 탈출
    if len(winning_nums) == 6:
        break
print(f"이번회차 당첨번호: {winning_nums}")
# 2. 번호6개 찍기 - 중복x
my_nums = []
while True:
    print(f"내가 뽑은 번호: {my_nums}")
    number = input("번호를 입력하세요>>")
    if not number.isdecimal():
        print("숫자를 입력하세요!")
        continue
    number = int(number)

    if not (1 <= number <= 45):
        print("1에서 45 사이값을 입력하세요")
        continue
    if number in my_nums:
        continue

    my_nums.append(number)
    if len(my_nums) == 6:
        print(f"내가 뽑은 번호: {my_nums}")
        break


# 3. 두개 비교하기
# 맞춘횟수 변수를 만들어서 두 리스트비교해서
# 같은값이 있으면 +1
winning_count = 0
for num1 in winning_nums:
    for num2 in my_nums:
        if num1 == num2:
            winning_count += 1

if winning_count == 6:
    print("1등입니다!")
elif winning_count == 5:
    print("2등입니다!")
elif winning_count == 4:
    print("3등입니다!")
else:
    print("꽝입니다")


# 방법2
"""for num2 in my_nums:
    if nums in winning_nums:    
        winning_count += 1"""