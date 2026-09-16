def print_matrix(m: list[list[int]]) -> None:
    for row in m:
        print(' '.join(map(str, row)))
    print()


def invert_columns(m: list[list[int]]) -> None:
    for row in m:
        i, j = 0, len(row)-1

        while i < j:
            row[i], row[j] = row[j], row[i]
            i+=1
            j-=1


def rotate_matrix(m: list[list[int]]) -> list[list[int]]:
    new_m = [[0 for _ in m] for _ in m[0]]
    i, j = 0, 0

    while i < len(m):
        while j < len(m[i]):
            new_m[j][i] = m[i][j]
            j+=1
        j=0
        i+=1

    invert_columns(new_m)

    return new_m


m = [[1, 2, 3], [4, 5, 6]]

print_matrix(m)
m = rotate_matrix(m)
print_matrix(m)
m = rotate_matrix(m)
print_matrix(m)
m = rotate_matrix(m)
print_matrix(m)
m = rotate_matrix(m)
print_matrix(m)
