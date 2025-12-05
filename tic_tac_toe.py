class board: 

    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.player='O'


    def eingabe(self):

        # changing the Player
        if self.player == 'x':
            self.player = 'O'
        else:
            self.player = 'x'


        # input the row and colum
        while True:
            try:
                row = int(input('gib eine Zeile ein (0-2): '))
                if 0 <= row <= 2:
                    break  # gültig, Schleife verlassen
                else:
                    print('Ungültig, nur 0, 1 oder 2 erlaubt!')
            except ValueError:
                print('Falsche Eingabe, bitte eine Zahl eingeben.')

        while True:
            try:
                colum = int(input('gib eine Spalte ein (0-2): '))
                if 0 <= colum <= 2:
                    break
                else:
                    print('Ungültig, nur 0, 1 oder 2 erlaubt!')
            except ValueError:
                print('Falsche Eingabe, bitte eine Zahl eingeben.')  

        # print the input
        print(f'Player {self.player} wählt row = {row} & colum = {colum}')


        # Feld schon besetzt
        if self.board[row][colum] != ' ':
            print("\nWenn wir Freunde wären würdest du so'n Scheiss überhaupt nicht machen")
            return self.eingabe()  # Spieler erneut wählen lassen

        # gültiger Zug
        self.board[row][colum] = self.player
        for i, line in enumerate(self.board):
            print(' | '.join(line))
            if i < 2:
                print('---------')  # Trenner zwischen den Reihen


        # Sieg prüfen
        if self.check():
            return True

        # Unentschieden prüfen
        if self.is_full():
            print("Unentschieden! Keine freien Felder mehr.")
            return True

        return False


    def check(self):
        # check rows
        if all(cell == self.player for cell in self.board[0]):
            return self.winning()
        elif all(cell == self.player for cell in self.board[1]):
            return self.winning()
        elif all(cell == self.player for cell in self.board[2]):
            return self.winning()

        # check colum
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == self.player:
            return self.winning()
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == self.player:
            return self.winning()
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == self.player:
            return self.winning()

        # check diagonal
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player:
            return self.winning()
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player:
            return self.winning()
        else:   
            return False

    
    def winning(self):
        print(f'Player {self.player} winns!!')
        return True
    
    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)



        
board = board()
print("Let' Play Tic-Tac-Toe")
while True:
   if board.eingabe():
       break