class Game():
    winning = [
        ['a1','b1','c1'],['a2','b2','c2'],['a3','b3','c3'],
        ['a1','a2','a3'],['b1','b2','b3'],['c1','c2','c3'],
        ['a1','b2','c3'],['c1','b2','a3']
    ]
    player_x_wins = 0
    player_o_wins = 0
    player_x_losses = 0
    player_o_losses = 0

    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print('Tic-Tac-Toe inbound!')
        while self.winner == None and self.tie == False:
            Game.render(self)
            Game.place_piece(self)
            Game.check_for_winner(self)
            Game.check_for_tie(self)
            Game.turn_change(self)
        Game.render(self)

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
          """)
        
    def print_message(self):
        if(self.tie):
            print("The game has ended in a tie!")
        elif(self.winner):
            print(f"{self.winner} wins!")
            if(self.winner == "X"):
                self.player_o_losses += 1
                self.player_x_wins += 1
            elif(self.winner == "O"):
                self.player_o_wins += 1
                self.player_x_losses += 1
            print(f"X player wins: {self.player_x_wins}, X player losses: {self.player_x_losses}")
            print(f"O player wins: {self.player_o_wins}, O player losses: {self.player_o_losses}")
            rematch = input("Would you like to play again? (Y/N/Yes/No) ").lower()
            if(rematch == "y" or rematch == "yes"):
                self.__init__()
                self.play_game()
        else:
            print(f"It's player {self.turn}'s turn.")

    def render(self):
        Game.print_board(self)
        Game.print_message(self)
    
    def place_piece(self):
        while True:
            self.move = input(f"Enter a valid movie (example: A1): ").lower()
            if(self.move in self.board and not self.board[self.move]):
                self.board[self.move] = self.turn
                break
            else:
                print("Invalid input")
    def check_for_winner(self):
        for win in Game.winning:
            if(self.board[win[0]] and self.board[win[0]] == self.board[win[1]] and self.board[win[0]] == self.board[win[2]]):
                self.winner = self.turn

    def check_for_tie(self):
        if(not None in self.board.values() and self.winner == None):
            self.tie = True
    
    def turn_change(self):
        if(self.turn == "X"):
            self.turn = "O"
        elif (self.turn == "O"):
            self.turn = "X"

game_instance = Game()
game_instance.play_game()