import sys

input_num = int(sys.stdin.readline())
for i in range(input_num):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)