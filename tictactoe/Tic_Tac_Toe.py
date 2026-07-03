

import math

EMPTY = " "


class TicTacToe:
    def __init__(self):
        self.board = [EMPTY] * 9
        self.human = "X"
        self.ai = "O"

   
    def print_board(self):
        print()
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")
        print()

   

  
    def check_winner(self):
        winning_combinations = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for combo in winning_combinations:
            a, b, c = combo

            if (
                self.board[a] == self.board[b] ==
                self.board[c] != EMPTY
            ):
                return self.board[a]

        return None


    

    def is_draw(self):
        return EMPTY not in self.board and self.check_winner() is None


   

    def available_moves(self):
        return [i for i in range(9) if self.board[i] == EMPTY]


    

    def minimax(self, depth, is_maximizing, alpha, beta):

        winner = self.check_winner()

        
        if winner == self.ai:
            return 10 - depth

        if winner == self.human:
            return depth - 10

        if self.is_draw():
            return 0

        
        if is_maximizing:
            best_score = -math.inf

            for move in self.available_moves():
                self.board[move] = self.ai

                score = self.minimax(
                    depth + 1,
                    False,
                    alpha,
                    beta
                )

                self.board[move] = EMPTY

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                # Alpha-Beta Pruning
                if beta <= alpha:
                    break

            return best_score

       
        else:
            best_score = math.inf

            for move in self.available_moves():
                self.board[move] = self.human

                score = self.minimax(
                    depth + 1,
                    True,
                    alpha,
                    beta
                )

                self.board[move] = EMPTY

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                # Alpha-Beta Pruning
                if beta <= alpha:
                    break

            return best_score


    
    
    def best_move(self):
        best_score = -math.inf
        best_move = None

        for move in self.available_moves():

            self.board[move] = self.ai

            score = self.minimax(
                depth=0,
                is_maximizing=False,
                alpha=-math.inf,
                beta=math.inf
            )

            self.board[move] = EMPTY

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

  
    

    def human_move(self):
        while True:
            try:
                move = int(input("Enter position (1-9): ")) - 1

                if move < 0 or move > 8:
                    print("Choose a number between 1 and 9.")
                    continue

                if self.board[move] != EMPTY:
                    print("That position is already occupied.")
                    continue

                self.board[move] = self.human
                break

            except ValueError:
                print("Please enter a valid number.")


    

    def ai_move(self):
        move = self.best_move()
        self.board[move] = self.ai
        print(f"\nAI chooses position {move + 1}")

  
    
  
    def play(self):

        print("=" * 45)
        print("      TIC-TAC-TOE AI")
        print(" Minimax + Alpha-Beta Pruning")
        print("=" * 45)

        print("\nBoard Positions:")
        print("1 | 2 | 3")
        print("4 | 5 | 6")
        print("7 | 8 | 9")

        
        while True:
            symbol = input("\nChoose your symbol (X/O): ").upper()

            if symbol in ["X", "O"]:
                break

            print("Invalid choice! Enter X or O.")

        if symbol == "X":
            self.human = "X"
            self.ai = "O"
        else:
            self.human = "O"
            self.ai = "X"

        
        while True:
            first = input(
                "Who plays first? (H = Human, A = AI): "
            ).upper()

            if first in ["H", "A"]:
                break

            print("Invalid choice! Enter H or A.")

        human_turn = (first == "H")

        print(f"\nYou are: {self.human}")
        print(f"AI is: {self.ai}")

        self.print_board()

        
        while True:

            if human_turn:
                self.human_move()
                self.print_board()

                if self.check_winner() == self.human:
                    print("🎉 Congratulations! You win!")
                    break

            else:
                self.ai_move()
                self.print_board()

                if self.check_winner() == self.ai:
                    print("🤖 AI Wins!")
                    break

            if self.is_draw():
                print("🤝 It's a Draw!")
                break

            human_turn = not human_turn




if __name__ == "__main__":
    game = TicTacToe()
    game.play()