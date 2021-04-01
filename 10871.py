n, x = map(int, input().split(' '))
li = list(map(int, input().split(' ')))

for i in range(n):
    if x > li[i]:
        print(li[i], end=' ')