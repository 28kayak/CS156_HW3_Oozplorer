__author__ = 'kaya'
import math
import random
import sys

class Agent:
    x = 0
    y = 0
    n = 0
    b =0
    def __init__(self, number, board):
        self.n = number
        self.b = board

    def start(self):
        status = 0
        sensor = 0
        while status == 0:
            try:
                i = random.randint(0,3)
                j = random.randint(0,3)
                (sensor, status) = self.b.move((i,j))
                self.b.print_board()
                print sensor
                print status
            except Exception as inst:
                print inst
        if status == 1:
            print "you win!"
        else:
            print "you lose!"
class Board:
    n = 0
    board = []
    def __init__(self,x):
        #initialize a board and fill up rooms by '.'
        self.n = x
        for i in range(self.n):
            self.board.append([])
        for i in range(self.n):
            for j in range(self.n):
                self.board[i].append([])
        for i in range(self.n):
            for j in range(self.n):
                self.board[i][j] = '.'
        #Assign P as pits and G as gold in random room
        self.board[random.randint(0, self.n - 1)][random.randint(0, self.n - 1)] = 'P'
        self.board[random.randint(0, self.n - 1)][random.randint(0, self.n - 1)] = 'P'
        self.board[random.randint(0, self.n - 1)][random.randint(0, self.n - 1)] = 'P'
        self.board[random.randint(0, self.n - 1)][random.randint(0, self.n - 1)] = 'G'
        self.board[0][0] = '@'
        print "Start Position"
        print
        self.print_board()
        print
        print "Start Game.........."

    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                sys.stdout.write(self.board[self.n - i - 1][j])
                sys.stdout.write('')
            print
        print
    def move(self, pair):
        (x,y) = pair
        neighbor = 0
        pit = 0
        sensor = False
        status = 0
        #check if the current room has a notation
        x1 = x
        y1 = y
        if x1 >= 0 and x1 < self.n and y1 >= 0 and y1 < self.n:
            if self.board[x1][y1] == '@':
                neighbor += 1
            if self.board[x1][y1] == 'P':
                pit += 1
        #check if the
        x1 = x + 1
        y1 = y
        if x1 >= 0 and x1 < self.n and y1 >= 0 and y1 < self.n:
            if self.board[x1][y1] == '@':
                neighbor += 1
            if self.board[x1][y1] == 'P':
                pit += 1
        x1 = x - 1
        y1 = y
        if x1 >= 0 and x1 < self.n and y1 >= 0 and y1 < self.n:
            if self.board[x1][y1] == '@':
                neighbor += 1
            if self.board[x1][y1] == 'P':
                pit+= 1
        x1 = x
        y1 = y -1
        if x1 >= 0 and x1 < self.n and y1 >= 0 and y1 < self.n:
            if self.board[x1][y1] == '@':
                neighbor += 1
            if self.board[x1][y1] == 'P':
                pit += 1
        if neighbor == 0:
            raise Exception('Error', 'move location error')
        if pit > 0:
            sensor = True
        if self.board[x][y] == 'G':
            status = 1
        if self.board[x][y] == '@':
            status = -1

        self.board[x][y] = '@'
        return (sensor, status)
number = 4
b = Board(number)
a = Agent(number, b)
a.start()





