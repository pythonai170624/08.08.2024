# pip install tkinter
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = 'X'
        self.board = ['' for _ in range(9)]
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font=('normal', 40), width=5, height=2,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_click(self, index):
        if self.buttons[index]['text'] == '' and self.check_winner() is None:
            self.buttons[index]['text'] = self.player
            self.board[index] = self.player
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.reset_game()
            elif '' not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_winner(self):
        return None

    def reset_game(self):
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button['text'] = ''
        self.player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
