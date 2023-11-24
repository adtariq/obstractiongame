from distutils.command.build_scripts import first_line_re
from board.board import Board
#from game import GameException
import random
import os
import sys
NUM_PLAYERS=2
class UI:
    def __init__(self,board):
        self.__board=board
        self.__name=""
    def game_on(self):
        x=''
        y=0
        try:
           
            while True:
                            
                print("************Board Dimensions************")
                print("*****for dimension from 4x4 to 9x9****")
                print("Length must be in alphabet fron D to I:")
                x=input("Enter Length for Board Dimension:")
                if x in ['D','E','F','G','H','I'] or x in ['d','e','f','g','h','i']:
                    print("Height must be in Numeric from 3 to 9:")
                    y=int(input("Enter Height for board Dimenrion:"))
                    if  y>=3 and y<=9:
                        self.__board = Board(x,y+1 )
                        self.pvc()
                else:
                    print(f"Please enter Valid Length /Hight dimension!")

                    # else: 
                    #     raise GameException("wrong option")
        except Exception as e:
            print(e)

    def pvc(self):
        ok=True
        print(self.__board.str())
        while ok:
            try:
                col=''
                row=0
                first_turn=random.randint(0,NUM_PLAYERS-1)
                colrow=input(f"Player {first_turn} turn! Insert the Coloumn and Row like 'C3...' :").strip()
                for i in colrow:
                    if i.isalpha():
                        col=i.upper()
                    else:
                        row=i
                
                if first_turn==0 or first_turn==1:
                    self.__board.First_move(col,row)
                    print(self.__board.str())
                    if self.__board.check()==True:
                        print(f"player-{first_turn}, won the game by Opposite player")
                        ch=input("Press any key to continue(y/n)")
                        if ch=='n' or ch=='N':
                            sys.exit()
                        os.system("clear")
                        return

                    print("Opposite player turn")
                    self.__board.last_move()
                    print(self.__board.str())
                    if self.__board.check()==True:
                        print(f"The Opposite player wons the game by player-{first_turn}")
                        ch=input("Press any key to continue(y/n)")
                        if ch=='n' or ch=='N':
                            sys.exit()
                        os.system("clear")
                        return
                
            except Exception as e:
                print(f"Exception: {e}")




