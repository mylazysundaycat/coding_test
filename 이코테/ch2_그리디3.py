# Q3
# N 행의 갯수 M 열의 갯수

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
