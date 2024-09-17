import utils as ut

def main():
    prepare_game

         
# First value is the number of cols and the second is the number rows
# In this case we are creating an bidimensional array of 8 x 8
def prepare_game():
    board = [["*" if i%2 == 0 else "_" for i in range(8)] for j in range(8)]
    print(board)

if __name__ == "__main__":
    main()