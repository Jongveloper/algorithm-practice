input_num = input().split(' ')
a = int(input_num[0])
b = int(input_num[1])
c = int(input_num[2])
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b)% c)
print(((a % c) * (b % c)) % c)