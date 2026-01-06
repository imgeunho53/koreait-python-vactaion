import random # 외부에서 코드를 빌려오는 것

# random.randint(1, 6) -> 1~6사이 랜덤 숫자 생성
my_random = random.randint(1,6)
fruits = ["사과", " 바나나", "포도", "배"]
random_fruit = random.choice(fruits) # 리스트 중 무작위 하나 선택

# 업다운게임
answer_num = random.randint(1, 100)

"""
while True:
        my_guess = int(input("1~100 사이 숫자를 입력 >"))
    # 문자열.isdecimal(): 0~9 문자로 이루어졌는가?
        if not my_guess.isdeciaml:
            print("숫자만 입력하세요")
            continue

        if my_guess > answer_num:
             print("다운!")
        elif my_guess < answer_num:
            print("업!")
        else:
            print(f"정답:{my_guess}")
            break
"""
# 가위 바위 보
# 3판 2선
# 사용자점수, 컴퓨터점수가 있고 먼저 2점을 획득하면 승리
가위바위보 = ["가위","바위","보"]
나의선택 = ""
컴퓨터선택 = ""
사용자점수 = 0
컴퓨터점수 = 0
while True:
    나의선택 = input("가위, 바위, 보 중 하나를 입력해 주세요>")
    나의선택 = 나의선택.strip() # 공백제거

    # 입력값 검증
    if 나의선택 not in 가위바위보:
        print("다시 입력하세요")
        continue

    컴퓨터선택 = random.choice(가위바위보)
    승리조건1 = 나의선택 == "가위" and 컴퓨터선택 =="보"
    승리조건2 = 나의선택 == "보" and 컴퓨터선택 == "바위"
    승리조건3 = 나의선택 == "바위" and 컴퓨터선택 == "가위"

    if 나의선택 == 컴퓨터선택:
        print("무승부")
        continue
    elif 승리조건1 or 승리조건2 or 승리조건3:
        print("승리")
        사용자점수 +=1

    else:
        print("패배")
        컴퓨터점수 +=1
    print(f"사용자점수:{사용자점수}, 컴퓨터점수:{컴퓨터점수}")

    if 사용자점수 == 2:
        print("사용자 승리")
        break
    elif 컴퓨터점수 == 2:
        print("컴퓨터 승리")
        break







