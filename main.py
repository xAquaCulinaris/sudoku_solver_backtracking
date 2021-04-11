blue = '\033[96m'
green = '\033[92m'
red = '\033[91m'
end = '\033[0m'

field = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def check_row(board, x):
    is_there = []
    for y in range(len(board)):
        if board[x][y] != 0:
            is_there.append(board[x][y])

    return len(is_there) == len(set(is_there))


def check_column(board, y):
    is_there = []
    for x in range(len(board)):
        if board[x][y] != 0:
            is_there.append(board[x][y])

    return len(is_there) == len(set(is_there))


def check_box(board, a, b):
    is_there = []
    for x in range(a, a + 3):
        for y in range(b, b + 3):
            if board[x][y] != 0:
                is_there.append(board[x][y])

    return len(is_there) == len(set(is_there))


def get_box_begin(a, b):
    while a % 3 != 0:
        a -= 1

    while b % 3 != 0:
        b -= 1

    return a, b


def validate(board, x, y):
    box_begin = get_box_begin(x, y)
    return check_row(board, x) and check_column(board, y) and check_box(board, box_begin[0], box_begin[1])


def solve(board):
    print_field(board)
    # get next empty field
    empty_field = find_empty(board)
    # when every field is solved return
    if not empty_field:
        return True
    else:
        x, y = empty_field

    for num in range(1, 10):
        board[x][y] = num
        if validate(board, x, y):
            if solve(board):
                return True

            board[x][y] = 0
        else:
            board[x][y] = 0
    return False


def find_empty(board):
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 0:
                return x, y
    return None


def print_separation():
    for x in range(15):
        print("_", end='')


def print_field(board):
    print("\n\nBoard: ", end='')
    for x in range(len(board)):
        print("")
        if x % 3 == 0 and x != 0:
            print_separation()
            print("")

        for y in range(len(board)):
            if y % 3 == 0 and y != 0:
                print(" | ", end='')
            if board[x][y] == 0:
                print(blue + str(board[x][y]) + end, end='')
            else:
                print(board[x][y], end='')


def main():
    solve(field)


if __name__ == '__main__':
    main()
