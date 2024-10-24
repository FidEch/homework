first= int(input("Введите первое число: "))
second= int(input("Введите второе число: "))
third= int(input("Введите третье число: "))
if first==second and second==third:
    print(int(3))
elif first==second or second==third or first==third:
    print(int(2))
else:
    print(int(0))