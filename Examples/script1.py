import numpy as np

class Board:
    def __init__(self,dim=3):
        self.board_array=np.array([[None,None,None]],
                                  [[None,None,None]],
                                  [[None,None,None]]
                                  )
        self.is_full=False
        self.symbol1='X'
        self.symbol2="O"
        self.dim=dim

    def is_full(self):
        return np.sum(self.board_array!=None) == self.dim ** 2

    def check_rows(self):
        pass

    def check_cols(self):
        pass

    def check_diagonals(self):
        pass

    def has_won(self,symbol_idx):
        
        any(check....) = true -> exit 


class Person:
    def __init__(self):
        pass

    def get_name(self):
        pass

# ----
# init

# loop until Board.is_full or Boad.has_won