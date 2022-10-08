# Q1


n = int(input("NxN지도를 입력하시오:"))
x, y = 1, 1
plans = input("이동경로를 입력하시오:").split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)