import random
import math
import asyncio
import sys

class Game:
    def __init__(self, sendData):
        self.sendData = sendData
        self.running = True
        self.direction = 2
        self.direction2 = 2
        self.score = 0
        self.score2 = 0
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.block_width = self.WIDTH/35
        self.block_height = self.HEIGHT/35
        self.block_width = math.floor(self.block_width)
        self.block_height = math.floor(self.block_height)
        self.TICKRATE = 9

    def checkEndGame(self, score):
        if score == self.block_height * self.block_width:
            return True
        
    def moveRight(self, snake, snake2):
        i,j = snake[0] 
        lenght = len(snake)
        a = lenght-1
        while a > 0:
            snake[a] = snake[a-1]
            a-=1
        if (i,j+1) in snake or (i,j+1) in snake2 or j+1 >= self.block_width or j+1 < 0 :
            print("Game Over")
            snake[0] = (i,j+1)
            return True
        snake[0] = (i,j+1)
        return False
        
        # snake.pop()
        # snake.append((i,j))
    def moveLeft(self, snake, snake2):
        i,j = snake[0] 
        lenght = len(snake)
        a = lenght-1
        while a > 0:
            snake[a] = snake[a-1]
            a-=1    
        if (i,j-1) in snake or (i,j-1) in snake2 or j-1 >= self.block_width or j-1 < 0:
            print("Game Over")
            snake[0] =  (i,j-1)
            return True
        snake[0] = (i,j-1)
        return False


    def moveDown(self, snake, snake2):
        i,j = snake[0] 
        lenght = len(snake)
        a = lenght-1
        while a > 0:
            snake[a] = snake[a-1]
            a-=1
        if (i+1,j) in snake or (i+1,j) in snake2 or i+1 >= self.block_height or i+1 < 0:
            print("Game Over")
            snake[0] =  (i+1,j)
            return True
        snake[0] =  (i+1,j)
        return False

    def moveUp(self, snake, snake2):
        i,j = snake[0] 
        lenght = len(snake)
        a = lenght-1
        while a > 0:
            snake[a] = snake[a-1]
            a-=1
        if (i-1,j) in snake or (i-1,j) in snake2 or i-1 >= self.block_height or i-1 < 0:
            print("Game Over")
            snake[0] =  (i-1,j)
            return True
        snake[0] =  (i-1,j)
        return False

    def move(self, snake, direction, snake2):
        if direction == 1:
            return self.moveUp(snake, snake2)
        if direction == 2:
            return self.moveRight(snake, snake2)
        if direction == 3:
            return self.moveDown(snake, snake2)
        if direction == 4:
            return self.moveLeft(snake, snake2)
        
        
    def addLenght(self, snake, direction):
        lenght = len(snake)
        i,j = snake[lenght-1]
        if direction == 1:
            snake.append((i-1,j))
        if direction == 2:
            snake.append((i,j+1))
        if direction == 3:
            snake.append((i+1,j))
        if direction == 4:
            snake.append((i,j-1))
        

    def generateSnack(self, snake):
        while True:
            i = random.randint(0, self.block_height-1)
            j = random.randint(0, self.block_width-1)
            if (i,j) not in snake:
                return i,j
    
            

    async def game_loop(self):
        print("RUNNING GAME LOOP")
        snake = [(2,2),(3,2),(2,3)]
        snake2 = [(5,2),(5,2),(5,3)]
        winner = 0

        i,j = self.generateSnack((snake+snake2))

        loop = asyncio.get_running_loop()

        while self.running:
            start = loop.time()
            gameOver = self.move(snake,self.direction,snake2)
            gameOver2 = self.move(snake2,self.direction2,snake)

            if (i,j) in snake:
                self.addLenght(snake,self.direction)
                self.score += 1
                i,j = self.generateSnack((snake+snake2))
            if (i,j) in snake2:
                self.addLenght(snake2,self.direction2)
                self.score2 += 1
                i,j = self.generateSnack((snake+snake2))
            gameOver3 = self.checkEndGame(self.score+self.score2)
            if gameOver:
                winner = 2
                print("Snake 2 wins")
                self.running = False
            if gameOver2:
                winner = 1
                print("Snake 1 wins")
                self.running = False
            if gameOver3:
                print("Game Over")
                print(f"Score p1: {self.score} Score p2: {self.score2}")
                winner = 3
                self.running = False

            self.sendData(snake,snake2,(i,j),winner)
            if not self.running:
                break
            elapsed = loop.time() - start
            await asyncio.sleep(max(0, 1/self.TICKRATE - elapsed))
