from numpy import random, ndarray
#print(np.__version__)
#random.choice() #random board
random.seed(0)
def build_board(size: int) -> ndarray:
    return random.choice(['Red', 'Black', 'Empty'], (size, size))
    #list_0_1 = np.array([[0, 1], [1, 0]])
    #checkerboard = np.tile(list_0_1, (n // 2, m // 2))
    #print(checkerboard.shape)
    #return checkerboard



def get_count(board: ndarray, match: str) -> int:
    return (board == match).sum()

if __name__ == '__main__':
    print("The checkers python file is not intended to be ran as __main__")
#check if running as a main and if so print file is not intended to be a if __name__ == '__main__'
