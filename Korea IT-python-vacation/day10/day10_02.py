# 함수 심화2
# 람다함수
# def로 정의해줘야하는데, 그럴필요없이 단순한 함수면
# 람다함수를 사용함
# 성능차이 x 간결하게 작성이 되지않으면 def쓰는걸 권장
def multiply(num1,num2):
    return num1*num2

lambda_multi = lambda num1, num2: num1*num2

print(multiply(1,2))
print(lambda_multi(1,2))

# 함수를 받는 함수 : 고차함수
# 함수를 매겨변수로 전달받아 호출하는 함수
def calc(num1,num2,fx):
    result = fx(num1,num2)
    return result
# 콜백함수 : 전달되는 함수
def plus(num1, num2):
    return num1+num2

calc_result = calc(10, 5 ,plus)
print(calc_result)
calc_result2 = calc(10,5,lambda num1,num2: num1+num2)
print(calc_result2)
# 람다함수와 자주쓰이는 내장함수
# 1.filter(): 함수결과가 True인 요소들만 남겨주는 함수
# filter(함수,리스트)
nums = [1,2,3,4,5]
calc_result3 = filter(lambda n: n % 2 ==0, nums)
# filter결과는 list로 형변환해야 리스트처럼 사용가능
calc_result3 = list(calc_result3)
print(calc_result3)

nums = [1,5,10,30,60,100]
# filter를 사용해서 10~60 사이 숫자들만 리스트로 모아서 출력
result = filter(lambda n : n>=10 and n<=60, nums)
result = list(result)
print(result)

