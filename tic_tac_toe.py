# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function for ... (displaying the board?)


class TicTacToe:
    def __init__(self):
        self.board_array=[
            [" "," "," "]
            [" "," "," "]
            [" "," "," "]
            ]
    def display_board(self):
        print(f"Current Board:")
        [print(self.board_array[row] for row in range(0,3))]

    def sum_rows(self,rowID):
        return sum(self.board_array[rowID]) 

    def sum_col(self,colID):
        return sum(self.board_array[0][colID] + self.board_array[1][colID]+self.board_array[2][colID])

    def is_full(self):

    def calculate_stat(self):
        pass

    



def create_board():
    pass


# Function for... (choosing a player?)
def blablabla():
    pass


# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":

    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    # info text
