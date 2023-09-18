mon = int(input("몇 월?: "))
if mon == 12 or mon == 1 or mon == 2:
    print("겨울")
elif 3 <= mon <= 5:
    print("봄")
elif 6 <= mon <= 8:
    print("여름")
else:
    print("가을")
    
mon = int(input("몇 월?: "))
if 3 <= mon <= 5:
    print("봄")
elif 6 <= mon <= 8:
    print("여름")
elif 9 <= mon <= 11:
    print("가을")
else:
    print("겨울")