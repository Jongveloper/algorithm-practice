a = int(input())
b = input() #b는 순서를 받아야하기 때문에 리스트형태로 냅둔다.

fir = a * int(b[2])
sec = a * int(b[1])
thr = a * int(b[0])

print(fir , sec, thr, a * int(b), sep='\n') # sep = '\n' 은 줄바꿈
