# Q3
# N 행의 갯수 M 열의 갯수

#나의 풀이
array_2D = [[1,2,3],
            [1,3,4],
            [4,3,6],
            [5,7,9]]
N = 4
M = 3
array_min = list()

for i in array_2D:
    i.sort()
    array_min.append(i[0])

array_min.sort()
print(array_min[N-1])


#풀이법1
n,m = map(int, input("행과 열을 입력하세요").split())

result = 0 

for i in range(n):
    array_2D = list(map(int, input("행 하나에 들어갈 숫자들을 입력하세요").split()))
    min_data = min(array_2D)
    result = max(result,min_data)

print(result)

