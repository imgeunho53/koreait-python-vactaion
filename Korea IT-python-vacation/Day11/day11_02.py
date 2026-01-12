# 객체지향 프로그래밍
# 데이터를 저장할때 안전하게 검증된 값만 저장하고 싶다
# 검증된 값들과 동작을 묶고 싶다.
from logging.config import ConvertingTuple


# 은행계좌 클래스
class BankAccount:
    def __init__(self, name):
        # 검증하는 코드 작성 가능
        self.name = name
        self.balance = 0 # 계좌개설시 무조건 0원

    def check_balance(self):
        print(f"{self.name}님의 잔액: {self.balance}")
    def deposit(self, amount):
        # amount가 숫자인지 검증
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액부족!")
            return
        # 검증 이후에 객체에 담긴 데이터를 조작할 수 있다.
        # 객체에 담긴 데이터는 언제나 신뢰가능하다.
        self.balance -= amount


class Cup:
    def __init__(self, size):
        self.size = size
        self.water = 0

    def check(self):
        print(f" 현재 물의양: {self.water}ml")

    def fill(self, amount):
        if amount + self.water > self.size:
            print("최대 용량이상을 채울수가 없습니다")
            return
        self.water += amount
    def drink(self, amount):
        if amount > self.water:
            print("물이부족합니다")
        self.water -= amount

cup1 = Cup(500)
cup1.fill(350)
cup1.drink(50)
cup1.check()

