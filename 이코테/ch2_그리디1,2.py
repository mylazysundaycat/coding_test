#그리디 알고리즘

#Q1
#500원,100원,50원,10원 동전 무수히 존재
#거슬러줘야할 돈은 N이고, N은 언제나 10의 배수이다.
#거슬러줘야할 동전의 최소갯수는?


from ast import Num


N=1260
coin=[500,100,50,10]
count=0
for i in coin:    
        count += N//i
        N %=  i
print("count:",count)


#POINT. 가장 큰 단위의 화폐부터 돈을 거슬러주는것 [큰 단위부터 나누는 것]
#가장 큰 단위가 작은 단위들이 배수이기 때문에 , 이러한 그리디 알고리즘 접근법이 가능함.


#Q2
#주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
#배열의 특정 인덱스에 해당하는 수가 연속해서  K번을 초과하면 안됨
#배열의 크기 N 숫자 더해지는 횟수 M 연속해서 초과하면 안되는 횟수 K

#첫번째 풀이
# M = 
# M=8 K=3
# M = K(M//K)+ (M-M//K)

M, K = map(int,input("M, K 를 입력하세요[띄어쓰기로 구분합니다]").split())
Number_array = list(map(int,input("리스트에 들어갈 숫자를 입력하세요[띄어쓰기로 구분합니다]").split()))
N = len(Number_array)
Number_array.sort()

sum = (M//K)*K*Number_array[N-1] + (M-(M//K)*K)*Number_array[N-2]
print(sum)


#두번째 풀이
M, K = map(int,input("M, K 를 입력하세요[띄어쓰기로 구분합니다]").split())
Number_array = list(map(int,input("리스트에 들어갈 숫자를 입력하세요[띄어쓰기로 구분합니다]").split()))
N = len(Number_array)
print("N:",N)
Number_array.sort()
sum = 0
print("Number_array : ", Number_array)
print("1번째로 큰 수 : ",Number_array[N-1])
print("2번째로 큰 수 : ",Number_array[N-2])
while True:
    for i in range(K):
        if M == 0:
            break
        sum += Number_array[N-1]
        M -= 1
    if M == 0:
        break
    sum += Number_array[N-2]
    M -= 1

print(sum)



#나의 풀이
M=8
K=3

Number_array = [3,3,5,8,9,2]
count=0
sum=0

Number_array.sort(reverse=True)
print(Number_array)
for i in range(M):
    if count < K+1:
        sum += Number_array[0]
        count += 1
    else:
        sum += Number_array[1]

print("sum : ",sum)


