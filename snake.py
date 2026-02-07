import pygame
import random

WIDTH = 700
HEIGHT = 700
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

snake = [(2,2),(3,2),(2,3)]

def drawSnake(snake):
    for i,j in snake:
        rect = pygame.Rect(j*35,i*35,35,35)
        pygame.draw.rect(screen,"purple",rect)

def moveRight(snake):
    i,j = snake[0] 
    lenght = len(snake)
    a = lenght-1
    while a > 0:
        snake[a] = snake[a-1]
        a-=1
    if (i,j+1) in snake or j+1 > 20 or j+1 < 0 :
        print("Game Over")
        snake[0] = (i,j+1)
        return True
    snake[0] = (i,j+1)
    return False
    
    # snake.pop()
    # snake.append((i,j))
def moveLeft(snake):
    i,j = snake[0] 
    lenght = len(snake)
    a = lenght-1
    while a > 0:
        snake[a] = snake[a-1]
        a-=1    
    if (i,j-1) in snake or j-1 > 20 or j-1 < 0:
        print("Game Over")
        snake[0] =  (i,j-1)
        return True
    snake[0] = (i,j-1)
    return False


def moveDown(snake):
    i,j = snake[0] 
    lenght = len(snake)
    a = lenght-1
    while a > 0:
        snake[a] = snake[a-1]
        a-=1
    if (i+1,j) in snake or i+1 > 20 or i+1 < 0:
        print("Game Over")
        snake[0] =  (i+1,j)
        return True
    snake[0] =  (i+1,j)
    return False

def moveUp(snake):
    i,j = snake[0] 
    lenght = len(snake)
    a = lenght-1
    while a > 0:
        snake[a] = snake[a-1]
        a-=1
    if (i-1,j) in snake or i-1 > 20 or i-1 < 0:
        print("Game Over")
        snake[0] =  (i-1,j)
        return True
    snake[0] =  (i-1,j)
    return False

def move(snake,direction):
    if direction == 1:
        return moveUp(snake)
    if direction == 2:
        return moveRight(snake)
    if direction == 3:
        return moveDown(snake)
    if direction == 4:
        return moveLeft(snake)
    
    
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
        i = random.randint(0,19)
        j = random.randint(0,19)
        if (i,j) not in snake:
            return i,j

def drawSnack(i,j):
    rect = pygame.Rect(j*35,i*35,35,35)
    pygame.draw.rect(screen,"green",rect)

def drawGrid():
    block = 35
    for x in range(0,WIDTH,block):
        for y in range(0,HEIGHT,block):
            rect = pygame.Rect(x,y,block,block)
            pygame.draw.rect(screen,"#002B6B",rect,1)
   
    
direction = 2
score = 0
gameOver = False
i,j = generateSnack(snake)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_0]:
        screen.fill("green")
        pygame.display.flip()
    if keys[pygame.K_w]:
        if direction is not 3:
            direction = 1
    if keys[pygame.K_s]:
        if direction is not 1:
            direction = 3
    if keys[pygame.K_d]:
        if direction is not 4:
            direction = 2
    if keys[pygame.K_a]:
       if direction is not 2:
            direction = 4
    if keys[pygame.K_q]:
       addLenght(snake,direction)

    screen.fill("black")
    drawGrid()
    gameOver = move(snake,direction)
    if gameOver:
        running = False
    drawSnake(snake)
    if (i,j) in snake:
        score+=1
        print(score)
        addLenght(snake,direction)
        i,j = generateSnack(snake)
    drawSnack(i,j)
    pygame.display.flip()
    clock.tick(9)