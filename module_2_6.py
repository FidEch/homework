def the_gate ():
    n = int(input('Enter n: '))
    password = []
    for i in range(n):
        for j in range(n):
            if i+j == n:
                if j > i:
                    password.append({i,j})
                if j < i:
                    continue
    print(*list(password))
the_gate()