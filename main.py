#import entire checkers library
import checkers


#The code must check if it’s running as main,
# and if so, call a function called game containing
# the main functionality, described next.


def game():
    board_size = float(input("Enter a board size between 4 and 16: "))
    if not 4 <= board_size <= 16:
        print(f"{board_size} is not a valid size. Enter a number between 4 and 16: ")
        board = checkers.build_board(board_size)
    else:
        print(board)
        for match in 'Empty', 'Black', 'Red':
            print("Number of empty cells: ", checkers.get_count(board, 'Empty'))


if __name__ == '__main__':
    game()
    #ask user for size of board
    #call the build_board function
    #print full board
    #print number of empty, black, and red cells using fuction from checkers.py