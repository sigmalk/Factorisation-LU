import numpy as np

dim = int(input('La dimension de la matrice à factoriser : '))
A = np.array([[int(input(f'A[{j + 1}][{i + 1}] = ')) for i in range(dim)] for j in range(dim)])
U = A
Id = np.eye(dim)
L = np.eye(dim)
El = []


def e_matrix(i, j, a):
    e = np.eye(a.shape[0])
    e[i-1, j-1] = - a[i-1, j-1] / a[j-1, j-1]
    return e


for i in range(dim):
    for j in range(dim):
        if i > j:
            El.append(e_matrix(i+1, j+1, A))

for i in range(len(El)):
    U = Id.dot(El[i].dot(U))

for i in range(dim):
    for j in range(dim):
        if i > j:
            L[i][j] = - e_matrix(i+1, j+1, A)[i][j]

print(f'U = {U} \n\n Et L = {L}')
