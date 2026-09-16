def transpose(m: list[list[int]]) -> None:
    i, j = 0, 0
    n = len(m)

    while i < n:
        while j < n:
            m[i][j], m[j][i] = m[j][i], m[i][j]
            j+=1
        i+=1
        j=i+1


def invert_columns(m: list[list[int]]) -> None:
    for row in m:
        i, j = 0, len(row)-1

        while i < j:
            row[i], row[j] = row[j], row[i]
            i+=1
            j-=1


def invert_rows(m: list[list[int]]) -> None:
    i, j = 0, len(m)-1

    while i < j:
        m[i], m[j] = m[j], m[i]
        i+=1
        j-=1


def rotate(m: list[list[int]], clockwise=True) -> None:
    transpose(m)

    if clockwise:
        invert_columns(m)
    else:
        invert_rows(m)


def print_matrix(m: list[list[int]]) -> None:
    for row in m:
        print(' '.join(map(str, row)))
    print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(matrix)
rotate(matrix)
print_matrix(matrix)
rotate(matrix, clockwise=False)
print_matrix(matrix)


