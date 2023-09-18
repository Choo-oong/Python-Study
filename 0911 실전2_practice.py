i = 0
while i < 11:
    i = i + 1
    print(i)

i = 1
while i % 2 == 0:
    i == 11
    break
    print(i)

i = 1
while i < 10:
    if i % 2 != 0:
        continue
    if i == 11:
        break
    print(i)


c = 1
while c < 11:
    c += 1
    if c % 3 == 0:
        print(c)

add = 0
for i in range(2, 11):
    add += 1

print(add)


i = 0
while i < 11:
    i += 1


i = 0
while i < 11:
    i += 1
    if(i == 4):
        break

count = int(input("출발하기 몇 초 전? "))
for i in range(count, 0, -1):
    print(i)
    i -= 1
    if i == 0:
        print("출발!")

n = int(input("숫자 입력: "))
while n >= 0:
    print("입력된 숫자는", n)
    if n < 0:
        print("종료")