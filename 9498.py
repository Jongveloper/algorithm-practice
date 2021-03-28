input_num = input().split(' ')
a = int(input_num[0])

if a >= 90:
    print("A")
elif 80 <= a <= 89:
    print("B")
elif 70 <= a <= 79:
    print("C")
elif 60 <= a <= 69:
    print("D")
else:
    print("F")