# Q4
# 1. N에서 1을 뺀다
# 2. N을 k로 나눈다
# N이 1이될때까지 시행하는 최소 횟수

# N = 19 K =3

n,k = map(int, input("N과 K를 입력하시오 : ").split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    if n<k:
        break
    result +=1
    n = n//k


result += (n-1)
print(result)


