#실전 1
#방법 1
print(3.14*float(input())**2)

#방법 2
radius = float(input())
print(3.14*radius**2)


#---------
#실전 2
print(int(input("정수를 입력하세요: "))**2)


#---------
#실전 3
#방법 1
num1 = float(input())
num2 = float(input())
num3 = float(input())
sum = int(num1 + num2 + num3)
average = sum/3
print(sum)
print(average)

#방법 2
num1 = int(input())
num2 = int(input())
num3 = int(input())
sum = num1 + num2 + num3
average = sum/3
print(sum)
print(average)


#---------
#실전 4
year = int(input("불기 연도를 입력하세요: "))
print(year-543)


#---------
#실전 5
sec1 = int(input("초를 입력하세요: "))

min = sec1//60
sec2 = sec1%60

print(sec1, "초(sec)는", min, "분(min)", sec2, "초(sec)입니다.")



#---------
#---------
#실전 1
num = int(input("숫자를 입력하세요: "))
if 10<num and num<20:
    print("True")
else:
    print("False")


#---------
#실전 2
num = int(input("숫자를 입력하세요: "))
if num < 0:
    print("음수")
elif num > 0:
    print("양수")
else:
    print("0")


#---------
#실전 3
num = int(input("숫자를 입력하세요: "))
if num %2 == 0:
    print("짝수")
else:
    print("홀수")


#---------
#실전 4
num1 = int(input("첫 번째 정수 입력: "))
num2 = int(input("두 번째 정수 입력: "))
num3 = int(input("세 번째 정수 입력: "))
if num1 % 2 != 0:
    print(num1)
if num2 % 2 != 0:
    print(num2)
if num3 % 2 != 0:
    print(num3)


#---------
#실전 5
result = int(input("코딩 테스트 점수 입력: "))
if result >= 90:
    print("A")
elif 80 <= result < 90:
    print("B")
elif 70 <= result < 80:
    print("C")
elif 60 <= result < 70:
    print("D")
else:
    print("E")


#---------
#실전 6
letter = input()
if letter == "a":
    print("ant")
elif letter == "b":
    print("bear")
elif letter == "c":
    print("cat")
elif letter == "d":
    print("dog")
else:
    print("error")


#---------
#실전 7
#방법 1
mon = int(input("몇 월?: "))
if mon == 12 or mon == 1 or mon == 2:
    print("겨울")
elif 3 <= mon <= 5:
    print("봄")
elif 6 <= mon <= 8:
    print("여름")
else:
    print("가을")
    
#방법 2
mon = int(input("몇 월?: "))
if 3 <= mon <= 5:
    print("봄")
elif 6 <= mon <= 8:
    print("여름")
elif 9 <= mon <= 11:
    print("가을")
else:
    print("겨울")

#정답
mon = int(input("몇 월?: "))
if mon == 12 or mon == 1 or mon == 2:
    print("겨울")
elif mon == 3 or mon == 4 or mon == 5:
    print("봄")
elif mon == 6 or mon == 7 or mon == 8:
    print("여름")
else:
    print("가을")