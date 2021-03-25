input_num = input().split(' ')
#split은 문자열을 공백 혹은 어떠한 기준으로 나눌 때 사용하는 함수이다.
#따라서 위의 코드는 무언가를 입력하고 스페이스바(공백)을하면 나눠진다는 뜻이다.
a = int(input_num[0]) # input 스페이스바(공백) 전 숫자.
b = int(input_num[1]) # input 스페이스바(공백) 후 숫자.
print(a + b)