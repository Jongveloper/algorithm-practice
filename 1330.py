input_num = input().split(' ')

a = int(input_num[0])
b = int(input_num[1])

if a > b:
    print(">")
elif a < b:
    print("<")
elif a == b:
    print("==")