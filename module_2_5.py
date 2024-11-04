
def get_matrix ():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    value = int(input("Enter value: "))
    matrix = [[value for _ in range(m)] for _ in range(n)]
    return matrix
print(get_matrix ())
