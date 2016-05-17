
#!/usr/bin/python
#Title: Simple Tic Tac Toe AI using Reinforcement Learning
#Date:17/5/2016
#Author:Adithya Selvaprithiviraj

import os

class TicTacToe():

    def __init__(self):
        
        os.system("clear")
        print "\nHi ! I am RL Tic Tac Toe and I learn as I play with you \n"
        while True:
            temp=int(input("Choose the symbol that you want to use! Enter\n [1] for X\n [2] for Y\n\n"))
            if temp == 1:
                self.player_symbol="X"
                self.Ai_symbol="O"
                break
            elif temp ==2:
                self.player_symbol="O"
                self.Ai_symbol="X"
                break
            else:
                print "Please Enter a Valid Choice\n"

        while True:
            temp=raw_input( "Do you want to play first ? (y/n) :\n\n" ).lower()

            if temp == "y":
                self.Ai_start=0
                break
            elif temp == "n":
                self.Ai_start=1
                break
            else:
                print "Please enter a valid choice\n"

        self.current_state=[" "]*9


    def displayBoard(self):
        """Displays Current Board view"""

        print "**-------------------------**\n"
        print "\t "+self.current_state[0]+" | "+self.current_state[1]+" | "+self.current_state[2]+ " " 
        print "\t-----------"
        print "\t "+self.current_state[3]+" | "+self.current_state[4]+" | "+self.current_state[5]+ " " 
        print "\t-----------"
        print "\t "+self.current_state[6]+" | "+self.current_state[7]+" | "+self.current_state[8]+ " \n" 
        print "**-------------------------**\n"


    def isBoardFull(self):
        """Returns if board is full or not"""

        if " " in self.current_state:
            return False
        else:
            return True

    def isWinning(self,player):
        """tells if particular position is winning for a player"""
        
        return((self.current_state[6]==player and  self.current_state[7] ==player and self.current_state[8])==player or \
                (self.current_state[0] ==player and  self.current_state[1]==player and self.current_state[2]==player) or \
                (self.current_state[2] ==player and  self.current_state[4]==player and self.current_state[6]==player) or \
                (self.current_state[0] ==player and  self.current_state[3]==player and self.current_state[6]==player) or \
                (self.current_state[2] ==player and  self.current_state[5]==player and self.current_state[8]==player) or \
                (self.current_state[3] ==player and  self.current_state[4]==player and self.current_state[5]==player) or \
                (self.current_state[1] ==player and  self.current_state[4]==player and self.current_state[7]==player) or \
                (self.current_state[0] ==player and  self.current_state[4]==player and self.current_state[8]==player))



    
    def getMove(self):
        """Gets a move from player"""

        temp=raw_input("\nEnter numbers from 1-9 to make a move ")
        try:
            if self.current_state[int(temp)-1] != " ":
                print "Position is already occupied, Please enter a valid move"
                self.getMove()

            else:
                self.current_state[int(temp)-1] = self.player_symbol
    
        except:
            print "Please enter a valid move"

    


a=TicTacToe()
a.displayBoard()


while not a.isBoardFull():

    a.getMove()
    a.displayBoard()
    if a.isWinning(a.player_symbol):
        print "Won"
        break

