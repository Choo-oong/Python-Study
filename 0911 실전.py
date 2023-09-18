#---조건문---
#실전 1
stature = int(input("키 입력: "))
if 150 <= stature <= 170 or 175 <= stature <= 180:
    print("탈 수 있다.")
else:
    print("탈 수 없다.")


#---------
#실전 2
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 <= 150:
    print("터널 통과 불가능")
elif n2 <= 150:
    print("터널 통과 불가능")
elif n3 <= 150:
    print("터널 통과 불가능")
else:
    print("터널 통과 가능")


#---------
#실전 3
a = int(input("수축기 혈압을 입력하세요: "))
b = int(input("이완기 혈압을 입력하세요: "))

if (a >= 160) and (b >= 100):
    print("2기 고혈압")
elif (140 <= a <= 159) or (90 <= b <= 99):
    print("1기 고혈압")
elif (120 <= a <= 139) or (80 <= b <= 89):
    print("고혈압 전 단계")
else:
    print("정상")


#---------
#실전 4
year = int(input("1 이상, 4000 이하의 자연수를 입력하세요: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("1")
else:
    print("0")


#---------
#실전 5
x = int(input("x 좌표를 입력하세요: "))
y = int(input("y 좌표를 입력하세요: "))

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


#---------
#실전 6
A = int(input())
operate = input()
B = int(input())

if operate == "*":
    print(A*B)
else:
    print(A+B)


#---------
#실전 6