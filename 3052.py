a_list = []
for i in range(10):
    input_num = int(input())
    a_list.append(input_num % 42)
a_list = set(a_list)
print(len(a_list))