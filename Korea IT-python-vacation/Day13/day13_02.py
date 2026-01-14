# 클래스 변수
# 클래스내부에도 데이터를 저장할 수 있음
# 해당 클래스 객체들은 다 공유

class Student:
    # 클래스변수
    school_name = "파이썬 고등학교"
    count = 0
    def __init__(self, name):
        self.name = name # 객체(인스턴스) 변수
        Student.count += 1
        # 정원 100명만 받겠다
        if Student.count >100:
            print("정원 초과! 현재 100명")
            # 예외(에러)를 고의로 일으켜야한다

st1 = Student("김학생")
st2 = Student("박학생")
print(st1.name)
print(st1.school_name) # 클래스변수 접근"만"가능
print(st2.school_name) # 동일한 변수에 접근"만 가능

# 데이터의 실제 메모리 주소
id_1 = id(st1.school_name)
id_2 = id(st2.school_name)
print(id_1)
print(id_2)

# 객체로 접근하여서 클래스변수 변경은 불가능
st1.name = "김학생아님" #필드값 변경
print(st1.name)
# 클래스변수 변경이 아니라 st1에 school_name이라는 필드를 추가하는것으로 파이썬이 해석
st1.school_name = "파이썬대학교"
print(st1.school_name)
print(st2.school_name)

# 클래스 이름으로 접근해야 변경 가능
Student.school_name = "파이썬 대학교"
print(st2.school_name) # 클래스 변수 변경
print(st1.count)
print(st2.count)



class Wallet:
    # 공용 돈 -> 클래스변수
    total_money = 100000
    def __init__(self, name):
        self.name = name
        self.money = 0 # 지갑생성시 0원

    def __str__(self):
        return f"{self.name}의 소지금: {self.money}"

    def take_money(self,amount):
        # 공용돈을 내 지갑(money필드)에 옮기는 코드를 작성, 남은 공용돈보다 더 많은 금액을 가져갈순x
        if isinstance(amount,int):
            if amount > Wallet.total_money:         # 대소비교, 동일비교 ->읽기 / 객체로 접근해도 동일하게 동작
                print("공용돈보다 많은 돈을 가져갈수는 없습니다")
                return
            self.money += amount
            Wallet.total_money -= amount
            print(f"공용돈:{Wallet.total_money}")
        else:
            print("숫자를 입력하세요")



        pass

My1 = Wallet("jason")
My2 = Wallet("pork")
My1.take_money(100000)







































