# 모듈: .py파일, 함수 or 클래스 정의만 있음
# 패키지: 모듈들을 묶어놓은 폴더
# __init__.py 는 해당 폴더를 파이썬이 패키지로 인식

import random # random.py파일의 코드를 복붙한 것, 라이브러리는 from 생략 ok
from a import a # a패키지 안에 있는 a.py 복붙
from b import b

# a.py안에 있는 add함수 as 별명
from b.b import Person
if __name__ == '__main__':
    p1 = Person("바보", 20)
    p1.print_person()

