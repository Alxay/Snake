import pygame
import random
import math

WIDTH = 1920
HEIGHT = 1080
block_width = WIDTH/35
block_height = HEIGHT/35
block_width = math.floor(block_width)
block_height = math.floor(block_height)
space = HEIGHT // 7 

pygame.init()
pygame.display.set_caption('Snake by Alxay')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

cat = pygame.image.load('alxaycat2.png')
button1 = pygame.image.load('singleplayer.png')
button2 = pygame.image.load('2player.png')
button3 = pygame.image.load('multiplayer.png')
top = (HEIGHT - space *2 - button1.get_height() * 3)// 2
def displayImage(x,y,image):
    screen.blit(image, (x,y))

snake = [(2,2),(3,2),(2,3)]
snake2 = [(5,2),(5,2),(5,3)]



def drawSnake(snake):
    for i,j in snake:
        rect = pygame.Rect(j*35,i*35,35,35)
        pygame.draw.rect(screen,"purple",rect)

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


def drawSnack(i,j):
    rect = pygame.Rect(j*35,i*35,35,35)
    pygame.draw.rect(screen,"green",rect)

def drawGrid():
    block = 35
    for x in range(0,WIDTH,block):
        for y in range(0,HEIGHT,block):
            rect = pygame.Rect(x,y,block,block)
            pygame.draw.rect(screen,"#002B6B",rect,1)



def menu():
    running = True
    while running:
        screen.fill("#22B2EB") 
        displayImage(WIDTH // 2 - button1.get_width() // 2,top + space, button1)
        displayImage(WIDTH // 2 - button2.get_width() // 2, top + space*2, button2)
        displayImage(WIDTH // 2 - button3.get_width() // 2, top + space*3, button3)

        window_rect = screen.get_rect()

        button1_rect = button1.get_rect(topleft=(WIDTH // 2 - button1.get_width() // 2, top + space))
        button2_rect = button2.get_rect(topleft=(WIDTH // 2 - button2.get_width() // 2, top + space*2))
        button3_rect = button3.get_rect(topleft=(WIDTH // 2 - button3.get_width() // 2, top + space*3))
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # lewy klik
                if button1_rect.collidepoint(mouse_pos):
                    singleplayer()
                    running = False
                    return
                if button2_rect.collidepoint(mouse_pos):
                    twoplayer()
                    running = False
                    return
                if button3_rect.collidepoint(mouse_pos):
                    running = False
                    return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            singleplayer()
            running = False
        if keys[pygame.K_2]:
            twoplayer()
            running = False

        pygame.display.flip()
        clock.tick(9)
   
def singleplayer():
    running = True
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
            if direction != 3:
                direction = 1
        if keys[pygame.K_s]:
            if direction != 1:
                direction = 3
        if keys[pygame.K_d]:
            if direction != 4:
                direction = 2
        if keys[pygame.K_a]:
            if direction != 2:
                direction = 4
        if keys[pygame.K_q]:
            addLenght(snake,direction)

        screen.fill("black")
        drawGrid()
        gameOver = move(snake,direction,snake2)
        if gameOver:
            running = False
        drawSnake(snake)
        # drawSnake(snake2)
        # move(snake2,direction)
        if (i,j) in snake:
            score+=1
            print(score)
            addLenght(snake,direction)
            i,j = generateSnack(snake)
        drawSnack(i,j)
        # displayImage(x,y,cat)
        pygame.display.flip()
        clock.tick(9)


def twoplayer():
    running = True
    direction = 2
    direction2 = 2
    score = 0
    score2 = 0
    gameOver = False
    i,j = generateSnack(snake + snake2)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_0]:
            screen.fill("green")
            pygame.display.flip()
        if keys[pygame.K_w]:
            if direction != 3:
                direction = 1
        if keys[pygame.K_s]:
            if direction != 1:
                direction = 3
        if keys[pygame.K_d]:
            if direction != 4:
                direction = 2
        if keys[pygame.K_a]:
            if direction != 2:
                direction = 4
        if keys[pygame.K_UP]:
            if direction2 != 3:
                direction2 = 1
        if keys[pygame.K_DOWN]:
            if direction2 != 1:
                direction2 = 3
        if keys[pygame.K_RIGHT]:
            if direction2 != 4:
                direction2 = 2
        if keys[pygame.K_LEFT]:
            if direction2 != 2:
                direction2 = 4

        screen.fill("black")
        drawGrid()
        gameOver = move(snake,direction,snake2)
        gameOver2 = move(snake2,direction2,snake)
        if gameOver:
            print("Snake 1 loses")
            running = False
        if gameOver2:
            print("Snake 2 loses")
            running = False
        drawSnake(snake)
        drawSnake(snake2)
        # drawSnake(snake2)
        # move(snake2,direction)
        if (i,j) in snake:
            score+=1
            print(score)
            addLenght(snake,direction)
            i,j = generateSnack(snake + snake2)
        if (i,j) in snake2:
            score2+=1
            print(score2)
            addLenght(snake2,direction2)
            i,j = generateSnack(snake + snake2)
        drawSnack(i,j)
        # displayImage(x,y,cat)
        pygame.display.flip()
        clock.tick(9)

menu()