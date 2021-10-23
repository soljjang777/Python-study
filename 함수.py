# -*- coding: utf8 -*-\

def cal(num1,num2,op):
    """덧셈뺄샘"""
    if op == "+" :
        result = num1+num2
    elif op == "-":
        result = num1-num2
    return result

num1 = int(input("첫 번째 정수 입력>>")) #input받는 값은 정수임으로 int앞에쓰기
num2 =  int(input("두 번째 정수 입력>>"))
op = input("연산자 입력(+,-)>>")
result=cal(num1,num2,op) #cal함수를 선언해서 위의 cal함수를 호출
print("결과 : {}".format(result))