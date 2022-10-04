#매 상황에서 가장 큰 값만 고르는 알고리즘
#따라서 최적의 해를 보장할 수 없을 때가 많습니다.

#Q1
#거스름 돈: 문제 해결 아이디어
#N=1260
#N=500x2 + 100x2 + 50x1 + 10x1
#총6개의 동전을 사용
#큰 화폐단위부터 돈을 거슬러주면 최적의 해가 됨
#WHY???? 이 아이디어의 정당성을 검토할 수 있어야 함
#여기서 제시한 가장 큰 단위가 작은 단위들의 배수가 
#되므로 종합할 수 있는것
n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)
#화폐의 종류가 K라고 할떄 복잡도는 K이다


#Q2
#N=17, K=4
#1번과정 1번, 2번과정 2번 -> 총 3번 실행

N=25
K=4

N, K = map(int, input().split())

count=0

while True:
    if N%K != 0:
        N = N-1
        count += 1
    else:
        N = N/K
        count += 1
        if N == 1:
            break


print(count)

