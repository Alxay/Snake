import socket
import threading
import random
import math
import asyncio

clients = []
TICKRATE = 20

def handle_client(conn):
    print(conn)
    while True:
        message = conn.recv(1).decode()
        if not message:
            break
    clients.remove(conn)
    conn.close()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(('localhost',55400))
    server.listen(2)
    while True:
        client,adress = server.accept()
        connected_client = threading.Thread(target=handle_client,args=(client,))
        connected_client.start()
        clients.append(client)


WIDTH = 1920
HEIGHT = 1080
block_width = WIDTH/35
block_height = HEIGHT/35
block_width = math.floor(block_width)
block_height = math.floor(block_height)

def checkEndGame(score):
    if score == block_height*block_width:
        return True
    
def moveRight(snake,snake2):
    i,j = snake[0] 
    lenght = len(snake)
    a = lenght-1
    while a > 0:
        snake[a] = snake[a-1]
        a-=1
    if (i,j+1) in snake or (i,j+1) in snake2 or j+1 >= block_width or j+1 < 0 :
        print("Game Over")
        snake[0] = (i,j+1)
        return True
    snake[0] = (i,j+1)
    return False
    
    # snake.pop()
    # snake.append((i,j))
def moveLeft(snake,snake2):
    i,j = snake[0] 
    lenght = len(snake)
    a = lenght-1
    while a > 0:
        snake[a] = snake[a-1]
        a-=1    
    if (i,j-1) in snake or (i,j-1) in snake2 or j-1 >= block_width or j-1 < 0:
        print("Game Over")
        snake[0] =  (i,j-1)
        return True
    snake[0] = (i,j-1)
    return False


def moveDown(snake,snake2):
    i,j = snake[0] 
    lenght = len(snake)
    a = lenght-1
    while a > 0:
        snake[a] = snake[a-1]
        a-=1
    if (i+1,j) in snake or (i+1,j) in snake2 or i+1 >= block_height or i+1 < 0:
        print("Game Over")
        snake[0] =  (i+1,j)
        return True
    snake[0] =  (i+1,j)
    return False

def moveUp(snake,snake2):
    i,j = snake[0] 
    lenght = len(snake)
    a = lenght-1
    while a > 0:
        snake[a] = snake[a-1]
        a-=1
    if (i-1,j) in snake or (i-1,j) in snake2 or i-1 >= block_height or i-1 < 0:
        print("Game Over")
        snake[0] =  (i-1,j)
        return True
    snake[0] =  (i-1,j)
    return False

def move(snake,direction,snake2):
    if direction == 1:
        return moveUp(snake,snake2)
    if direction == 2:
        return moveRight(snake,snake2)
    if direction == 3:
        return moveDown(snake,snake2)
    if direction == 4:
        return moveLeft(snake,snake2)
    
    
def addLenght(snake,direction):
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
    

def generateSnack(snake):
    while True:
        i = random.randint(0,block_height-1)
        j = random.randint(0,block_width-1)
        if (i,j) not in snake:
            return i,j
        

async def game_loop():
    running = True
    gameOver = False
    gameOver2 = False
    score = 0
    score2 = 0
    direction = 2
    direction2 = 2
    snake = [(2,2),(3,2),(2,3)]
    snake2 = [(5,2),(5,2),(5,3)]

    i,j = generateSnack((snake+snake2))

    while running:
        gameOver = move(snake,direction,snake2)
        gameOver2 = move(snake2,direction2,snake)

        if (i,j) in snake:
            addLenght(snake,direction)
            score += 1
            i,j = generateSnack((snake+snake2))
        if (i,j) in snake2:
            addLenght(snake2,direction)
            score2 += 1
            i,j = generateSnack((snake+snake2))

        gameOver3 = checkEndGame(score+score2)
        if gameOver:
            print("Snake 2 wins")
        if gameOver2:
            print("Snake 1 wins")
        if gameOver3:
            print("Game Over")
            print(f"Score p1: {score} Score p2: {score2}")
            running = False
      
        await asyncio.sleep(1 / TICKRATE)


asyncio.run(game_loop())