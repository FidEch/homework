
def get_matrix (n,m,value):
    matrix = [[value for _ in range(m)] for _ in range(n)]
    return matrix
print(get_matrix (2, 5, 6 ))
