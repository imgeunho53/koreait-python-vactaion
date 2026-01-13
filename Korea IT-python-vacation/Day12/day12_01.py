# 상속
# 두개 이상의 클래스가 공통코드가 많을때
# 이를 상위클래스로 정의해서 묶어 줄수있음

class Pet:
    def __init__(self, name, age):
        print("부모클래스 생성자 호출!")
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}가 밥을 먹습니다")

class Dog(Pet):
    def sound(self):
        print(f"{self.name}가 짖습니다 멍멍")

class Cat(Pet):
    def sound(self):
        print(f"{self.name}가 짖습니다 야옹")
    # 부모의 함수를 재정의: 오버라이딩(overwriting)
    def eat(self):
        print("꺳잎 주세요")
# __init__ 을 정의하지 않음
# Dog와 Cat의 생성자를 호출했지만 # 부모클래스의 __init__이 호출 됨
dog = Dog("뽀삐", 5)
cat = Cat("나비",5)
dog.eat() # 부모클래스 eat
cat.eat()
dog.sound()
cat.sound()

# MRO(method resolution order)
# 자식클래스에 호출한 함수가 없으면
# 파이썬은 부모클랴스에 해당 함수를 찾으러 간다.
# 있으면 부모껄 호출

# 오버라이딩 활용
class Car:
    def __init__(self, name, model):
        print("부모클래스 생성자 호출!")
        self.name = name
        self.model = model

    def drive(self):
        print(f"{self.name}가 주행을 시작합니다.!")

# 상속받은 자식 객체는 super(부모) 클래스의 데이터 영역이 구분되어있다. 단, self의 데이터 영역은 super 객체의 데이터영역을 포함한다.
class ElectricCar(Car):
    # __init__을 재정의
    # super().__init__이 호출되어야함
    def __init__(self, name, model, battery):
        super().__init__(name, model) #클래스 "Car"에 __init__를 호출 실제로 electric(car)의 __init__과 Car의 __init__은 다름
        # super(): 부모의 메서드를 연결해주는 함수
        self.battery = battery
# 오버라이딩
    def drive(self):
        super().drive() # 부모의  drive
        print("전기로!!")



class GasCar(Car):
    # __init__을 재정의
    # super().__init__이 호출되어야함
    def __init__(self, name, model, gas):
        super().__init__(name, model) #클래스 "Car"에 __init__를 호출 실제로 electric(car)의 __init__과 Car의 __init__은 다름
        # super(): 부모의 메서드를 연결해주는 함수
        self.gas = gas
# 오버라이딩
    def drive(self):
        super().drive() # 부모의  drive
        print("휘발유로!!")
# 호출된 test_car는 같은코드
# 동작이 달라진다.
def test_car(car):
    # 검증코드필요
    # 매개변수로 들어온 car가 drive() 함수를 반드시 가지고 있길 바람
    # drive는 오버라이딩된 함수임
    # -> Car를 상속받은 객체인지만 확인하면 되겠다
    is_car_instance = isinstance(car,Car)
    if not is_car_instance:
        print("자동차가 아닙니다")
        return
    car.drive() #같은 함수 호출 중
    # drive라는 같은 함수 - > 다른 동작 # 다형성

eCar = ElectricCar("모델y", "tesla", 100)
gCar = GasCar("x3", "bmw", 100)

test_car(gCar)
test_car(eCar)


class Payment:
    def __init__(self):
        print("결제시스템 초기화")

    # pass - 나중에 구현하겠다 에러 방지용
    # 상속받은 자식클래스에서 오버라이딩하면
    # 호출안됨
    def pay(self, price):
        pass

# KakaoPayment - pay오버라이딩 15000원이상 결제시 5퍼 할인
# NaverPayment - pay오버라이딩 20000원이상 결제시 2000할인

class KakaoPayment(Payment):
    # 생성자 생략 - 생성자를 오버라이딩할때는 # super().__init__() 필요
    def pay(self,price):
        # super().pay() 는 필수 아님
        if price >= 15000:
            new_price = price * 0.95
            return new_price

        return price

class NaverPayment(Payment):
    def pay(self,price):
        if price >= 20000:
            new_price = price - 2000
            return new_price

        return price


def order(payment, price):
    is_payment = isinstance(payment,Payment)
    if not is_payment:
        print("올바른 결제방식을 선택하세요")
        return
    total_price = payment.pay(price)
    print(f"총 결제금액: {total_price}원")

kakao = KakaoPayment()
naver = NaverPayment()
order(kakao, 30000)
order(naver, 20000)

food_menu = {
    "피자": 25000,
    "치킨": 20000,
    "참치김밥": 5000,
    "라면": 4000,
    "제로콜라": 1500
}

# [{메뉴이름: 갯수}, {메뉴이름: 갯수}, {}]
# 위의 리스트를 받아서 결제 총금액을 리턴
def accept(menus):
    # 메뉴들에서 메뉴들을 골라 옴
    for menu in menus:
        price_sum = 0
        # menu -> {메뉴이름: 갯수}
        # menu.items() -> [{메뉴이름, 갯수}]
        for item_name, item_count  in menu.items():
            price = food_menu[item_name]
            price_sum += price * item_count

    return price_sum

cart = []
while(True):
    food_list = list(food_menu.keys())
    print(food_list)
    menu_name = input("담으실 메뉴를 입력하세요>")
    count = int(input(" 몇개 담으시겠습니까? >"))

    cart_item = {menu_name: count}
    cart.append(cart_item)

    confirm = input("주문을 마치시겟습니까?")
    if confirm.lower() == "y":
        break

print(cart)

total_price = accept(cart)
order(kakao, total_price)
order(naver, total_price)



