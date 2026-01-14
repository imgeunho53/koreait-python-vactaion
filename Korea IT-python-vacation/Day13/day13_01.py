# 매직 매서드
# 파이썬의 거의 대부분은 클래스로부터 만들어진 객체다

# 모든 클래스의 공통 조상 -> Object클래스
# Object를 상속받고 있다면, Object의 매서드를 호출할수있다.

# object상속은 생략가능
# Person() -> __init__ 호출됨
# person.__init__ 호출됨
class Person(object):
    # __어쪼고__() ---> 매직매서드
    # object에 정의 되어있던 __init__()를 오버라이드 하고 있었음
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # 객체를 출력할때(문자열화):
        return f'{self.name} is {self.age} years old'

    def __eq__(self, other): # == 연산시 호출
        if isinstance(other, Person):
            return self.age == other.age
        elif isinstance(other, int):
            return self.age == other
    # less than -> __lt__ -> "<"
    # greater than -> __gt__ -> ">"
    # less than or equal -> __le__ -> "<="
    # greater than or equal -> __ge__ -> ">="
    def __lt__(self,other): # < 연산시 호출
        print("나이비교")
        if isinstance(other, Person):
            return self.age < other.age
        elif isinstance(other, int):
            return self.age < other

    # "+" -> __add__ ,"-" -> __sub__, "*" -> __mul__ "/" -> __div__
    def __add__(self, other):
        if isinstance(other, int):
            new_age = self.age + other
            return new_age
p1 = Person("홍길동", 20)
p2 = Person("김길동", 20)
print(p1==p2)
print(p1 < 30)
p3 = p1 + 14
print(p3) # 리턴받은 제 3의 객체
print(p1)

# 좌표 클래스
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Coord):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Coord(new_x, new_y)
    def __sub__(self, other):
        if isinstance(other, Coord):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Coord(new_x, new_y)
    def __str__(self):
        coord_str = f"현재좌표: ({self.x}, {self.y})"
        return coord_str

    # 같은 Coord 객체끼리 연산!
    # == 연산시 x,y좌표 동일하면 true
    # + 연산시 x좌표 y좌표가 각각 더해지게
    # -연산시, x좌표 y좌표가 각각 빼지도록
    # 객체출력시, "현재좌표" : ({x좌표},{y좌표})
c1 = Coord(1, 2)
c2 = Coord(2, 2)
print(c1+c2)
print(c1 == c2)
print(c1 - c2)

print("hi" * 50) # str클래스에서 __mul__을 오버라이딩한거임
print([1,2,3]+[4,5,6]) #list클래스에서 __add__ 오버라이딩
















