from tkinter import *
from PIL import Image, ImageTk
import functools
import main

#Run this script to use the graphical user interface, or alternatively, 
#run main.py to use a command-line interface

window = Tk()
window.title("Tic tac toe")
window.iconbitmap(default="images/icon.ico")

imageNone = ImageTk.PhotoImage(Image.open('images/Empty.png').resize((100, 100)))
imageO = ImageTk.PhotoImage(Image.open('images/O.png').resize((100, 100)))
imageX = ImageTk.PhotoImage(Image.open('images/X.png').resize((100, 100)))


boardSquares = []

def renderBoard(board):
    for x in range(3):
        for y in range(3):
            square = board[x][y] 
            if square == 'X':
                image = imageX
            elif square == 'O':
                image = imageO
            else:
                image = imageNone
            button = Button(
                master=window,
                bg="#313B5C",
                fg="#313B5C",
                image= image,
                borderwidth=0,
                bd=0,
                command= functools.partial(buttonClick, index=(x,y))
            )
            button.grid(row=x, column=y)
            boardSquares.append(button)

def buttonClick(index):
    global player
    newBoard = main.makeMove(board, index, player)
    renderBoard(newBoard)
    winner = main.getWinner(newBoard)

    if winner is not None:
        #end
        openAlertWindow(winner + " wins!")

    if main.isBoardFull(newBoard):
        openAlertWindow("Draw")
        #end
    
    if(player == 'X'):
       player = 'O'
    else:
       player = 'X'

def openAlertWindow(message):
        global toplevel_window
        if toplevel_window is None or not toplevel_window.winfo_exists():
            toplevel_window = AlertWindow(message) 
            toplevel_window.protocol("WM_DELETE_WINDOW", toplevel_window.closeAlert)

        else:
            toplevel_window.focus()

class AlertWindow(Toplevel):
    def __init__(self, message):
        super().__init__()
        self.grab_set()
        self.geometry("200x100")
        self.title("")
        

        self.grid_columnconfigure(0, weight=1)
        self.messageText = Label(self, text=message)
        self.messageText.grid(row=0, column=0, padx=20, pady=20)

        self.retryButton = Button(self, text="Retry", command=self.closeAlert)
        self.retryButton.grid(row=1, column=0, padx=20, pady=0)
    
    def closeAlert(self):
        restart()
        self.destroy()
    
    
def restart():
    global board
    board = main.newBoard()
    global player
    player = 'X'
    renderBoard(board)



board = main.newBoard()
player = 'X'
toplevel_window = None

renderBoard(board)

window.mainloop()



