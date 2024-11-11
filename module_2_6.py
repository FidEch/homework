def the_gate ():
    gate_1 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    gate_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    password = []
    print(type(gate_1))
    print(type(gate_2))
    for i in range(len(gate_2)+1):
        for j in range(len(gate_2)+1):
            if i == 0 or j == 0:
                return password.append(i,j)
            print(password)