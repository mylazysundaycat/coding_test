#1. 실수형
#정수부가 0일 때 0을 생략
a = -.8
#지수 표현 방식
a = 3e5 # 3 X (10의5제곱) 
b = 1e9 # 10억 100000000.0 실수형으로 나옴
b = int(b) # 실수형을 정수형으로 표현
print(.3+.6)
#실행값이 0.8999가 나옴
print(round(0.3+0.6,4))






#2. 리스트 자료형
#자바의 Array와 비슷하다
#인덱스는 0부터 출발한다
#인덱스에는 양의 정수, 음의 정수 모두 가능함

#리스트 초기화
#직접 대입
a=[1,2,3,4,5]
#그 외
a=[0]*5
 
#리스트 불러오기
#하나의 원소
a=[1,2,3,4,5]
print(a[1])
#슬라이싱
print(a[1:4])

#리스트 컴프리헨션
array = [i for i in range(10)] #0부터9까지
print(array)
array2 = [i for i in range(20) if i%2 == 1]
print(array2)
array3 = [i*i for i in range(0,10)]
print(array3)

#2차원 리스트
array4 = [[0]*3 for _ in range(2)] #언더바?
print('array4',array4)

#파이썬의 언더바
#반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할때 언더바를 자주 사용합니다




#3. 튜플
#튜플은 한번 선언된 값을 변경할 수없다
#리스트에 비해서 공간 효율적이다
a=(1,2,3,4,5,6)
print(a[3])
print(a[0:3])
#변경이 불가능하므로 Key값으로 사용될 수 있다





#4. 사전 자료형 (Dictionary)
#키와 값의 쌍을 데이터로 가지는 자료형이다
#Key를 이용해서 Value에 접근할 수있다.
data = dict()
data['사과']='Apple'
data['바나나']='Banana'
#key 리스트
data_key= data.keys()
#value 리스트
data_value=data.values()
print(data_key)
a = [ i for i in data_key]
print(a)
for key in data_key:
    print(key)



#5. 집합자료형
# 중복허용X 순서X
# 데이터 조회 및 수정은 상수시간
data=set([1,2,3,4,4,6,4,2,1,2])
#합집합,교집합,차집합 연산 가능
#새로운 원소 추가
data.add(8)
#새로운 원소 여러개 추가
data.update([5,6])





#6.입출력
#input은 한 줄의 문자열을 입력받는 함수
#map은 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
#a = list(map(str,input().split()))
#print(a)
#print(type(a))
#입력을 빨리 받는 함수sys.stdin.readline()
from re import I
import sys
data = sys.stdin.readline().rstrip()
print(data)
#f-string
#문자열과 정수를 함께 넣을 수 있다.
answer=7
print(f"정답은{answer}입니다.")




#7.조건문
x=15
if x>=10:
    print("x>=10")
#비교연산자: 특정한 두 값을 비교할 때 이용
#논리연산자: True , False 비교시 사용
#pass 키워드: 아무것도 처리하고 싶지 않을 때 사용
#조건문 표현식
score=85
result= "Success" if score>80 else "Fail"
print(result)



#8.반복문
#while문과 for문이 있음
result=0
i=1
while i<=9:
    result+=i
    i=i+1
result=0
for i in range(0,10):
    result+=i
print(result)
array=[9,8,7,6,5]
for i in array:
    print(i)
#continue
#반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할때 사용함




#9. 함수
#특정한 작업을 하나의 단위로 묶어놓은 것
def add(a,b):
    return a+b
#global키워드
#함수 내에서 바깥 변수를 사용할때 사용함
#함수 내에선 지역변수>전역변수(함수밖변수)
#함수 밖에선 전역변수>지역변수
a=0
def func():
    global a
    a += 1
func()
print(a)
#여러개의 반환값
def operator(a,b):
    return a+b, a-b #패킹
a, b = operator(7,1)#언패킹
print(a,b)
#람다표현식
lambda a,b:a+b(3,3) #이름없는 함수
list1=[1,2,3]
list2=[3,2,1]
#람다의 활용
result = map(lambda a,b:a+b,list1,list2)





#10.라이브러리
#순열과 조합
#카운터
#최대 공약수와 최소 공배수

