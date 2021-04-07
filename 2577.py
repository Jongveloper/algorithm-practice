a = int(input())
b = int(input())
c = int(input())

multi = list(str(a*b*c))

for i in range(10):
    print(multi.count(str(i)))