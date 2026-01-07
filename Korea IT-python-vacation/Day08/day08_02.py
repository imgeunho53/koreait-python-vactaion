dialog = ("솔직히 말해서 솔직히 저는 이게 맞는지 모르겠습니다." 
          "솔직히 근데 그냥 솔직히 귀찮습니다.")
word = "솔직히"
# 솔직히 라는 단어는 몇번 반복되는지?
# 문장과 단어를 매개변수로 받고
# 단어가 문장안에서 몇번 등장하는지 리턴하는 함수

def dialogue(dialog, word):
    len_of_word = len(word)
    count = 0
    for i in range(len(dialog)):
        tmp = dialog[i:i+len_of_word]
        if tmp == word:
            count += 1

    return count
countA = dialogue(dialog, word)
print(countA)


# 할인계산기
menu = {
        1: ("아메리카노", 2500),
        2: ("카푸치노", 4000),
        3: ("바닐라라떼", 3500)
    }
menu_choice = input("메뉴를 선택하세요(1~3) >>")
menu_choice = int(menu_choice)
menu_name, price = menu[menu_choice]
day = input("오늘은 무슨 요일인가요(월~일)>")
# day를 매개변수로 전달받아서 월:10퍼 화~금:5퍼 토~일: 20퍼
def discount(price, day):
    day =  day.strip()
    if day == "월":
        return price * 0.9
    elif day in ["화","수","목","금"]:
        return price * 0.95
    else:
        return price * 0.8

discount_price = discount(price, day)
print(f"이 {menu_name}의 가격은 {discount_price}원입니다")
