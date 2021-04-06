a_list = []
for i in range(9):
    a_list.append(int(input()))
print(max(a_list))
print(a_list.index(max(a_list))+1)
#index 함수는 문자 및 문자열의 위치를 찾아준다.
#index는 문자열,리스트,튜플 자료형에서 사용가능
#index(i)는 리스트에 i값이 있으면 i값의 위치를 되돌려줌
#index는 기본 0부터 시작 문제에선 예제출력이 자릿수를 1부터 시작했기 때문에 index()+1