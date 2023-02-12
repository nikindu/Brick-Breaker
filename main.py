'''This program draws a ball, a controllable paddle, and breakable rows of bricks onto the screen
-The goal of the program is use the paddle to bounce the ball off of it and break all of the bricks
each brick makes your score go up by one, after breaking all the bricks the game will end in a win
-If the ball goes beneath the paddle it will lose a life
the ball has three lives in total, if the ball reaches zero lives, the game will end in a loss'''

#Import and initialize the pygame library and random library
import pygame
import random
#Initializing pygame package
pygame.init()
#Setting game run to True
running = True
#Game run speed
FPS = 120
fpsClock = pygame.time.Clock()
#Defining colours used in game
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
GREEN2 = (0, 255, 0)
BLUE = (135, 206, 235)
BLUE2 = (3, 5, 54)
YELLOW = (255, 255, 0)
#Setting background colour
bgColour = BLUE2
#Setting screen width and screen height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
#Initializing screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Brick Break')
screen.fill(bgColour)
pygame.display.flip()
#Loading images
Title = pygame.image.load('img/Title.png')
Win = pygame.image.load('img/Win.png')
#Ball configurations
ballRadius = 5
ballColour = WHITE
rectColour = GREEN
ballX = 200
ballY = 300
dx = 1
dy = 1
randNumPositive = random.randint(2, 3)
randNumNegative = random.randint(-3, -2)
#Rectangle and brick configurations
rectX = SCREEN_WIDTH - 350
rectY = SCREEN_HEIGHT - 50
rectWidth = 100
rectHeight = 10
brickW = 60
brickH = 20
#Amount of rows and columns of the brick formation
brickRows = 8
brickColumns = 5
#List containing all breakable bricks
brickList = []
#Total score and Lives
score = 0
lives = 3
'''Function that draws the breakable bricks at the top of the screen'''
def bricks():
    for i in range(brickRows):
        for j in range(brickColumns):
            rRed = random.randint(0, 255)
            rGreen = random.randint(0, 255)
            rBlue = random.randint(0, 255)
            brick = (i * (brickW + 10) + 20, j * (brickH + 10) + 60, brickW,
                     brickH)
            pygame.draw.rect(screen, (rRed, rGreen, rBlue), brick, 0)
            brickList.append(brick)

            
'''Function used to draw the ball'''
def drawBall(x, y, ballColour):
    global ball
    ball = pygame.draw.circle(screen, ballColour, (x, y), ballRadius)

    
'''Function used for drawing the paddle'''
def drawRect(rectX, rectY, rectColour):
    global myRect
    myRect = pygame.Rect(rectX, rectY, rectWidth, rectHeight)
    pygame.draw.rect(screen, rectColour, myRect)

    
'''Function used to draw title screen'''
def mainMenu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False
                elif event.key == pygame.K_q:
                    pygame.quit()

        screen.blit(Title, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 80)
        # Draws a rectangle that has text inside it
        text = font.render("Brick Breaker", True, GREEN2)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH / 2, 100)
        screen.blit(text, textRect)  # Puts the textbox on the screen

        font = pygame.font.Font('freesansbold.ttf', 30)
        text2 = font.render('Space to Start q to quit', True, RED)
        textRect2 = text.get_rect()
        textRect2.center = (400, 550)
        screen.blit(text2, textRect2)
        pygame.display.update()
    screen.fill(bgColour)
    pygame.display.update()

    
'''Function used to draw pause screen'''
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_RIGHT or pygame.K_LEFT:
                    paused = False

        font = pygame.font.Font('freesansbold.ttf', 60)
        # Draws a rectangle that has text inside it
        text = font.render("Paused", True, RED)
        screen.blit(text,
                    (SCREEN_WIDTH / 3, 200))  # Puts the textbox on the screen

        font = pygame.font.Font('freesansbold.ttf', 20)
        text2 = font.render("Press P or arrow keys to continue", True, GREEN)
        screen.blit(text2, (150, 350))
        pygame.display.update()
    screen.fill(bgColour, (SCREEN_WIDTH / 3, 200, 220, 60))
    screen.fill(bgColour, (150, 350, 440, 20))
    pygame.display.update()


'''Function used to draw game over screen'''
def gameOver():
    dead = True
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dead = False
                elif event.key == pygame.K_q:
                    dead = False
                    mainMenu()

        font = pygame.font.Font('freesansbold.ttf', 60)
        # Draws a rectangle that has text inside it
        text = font.render("GAME OVER", True, RED)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH / 2, 250)
        screen.blit(text, textRect)  # Puts the textbox on the screen

        font = pygame.font.Font('freesansbold.ttf', 30)
        text2 = font.render("Press Space to restart, press Q to quit", True,
                            GREEN)
        textRect2 = text.get_rect()
        textRect2.center = (210, 350)
        screen.blit(text2, textRect2)

        dis_score = font.render("Score: " + str(score), True, YELLOW)
        screen.blit(dis_score, (225, 400))

        screen.fill(bgColour, (0, SCREEN_HEIGHT - 595, 100, 30))
        screen.fill(bgColour, (500, SCREEN_HEIGHT - 595, 100, 30))
        pygame.display.update()
    screen.fill(bgColour)
    pygame.display.update()


'''Function used to draw win screen'''
def winScreen():
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    win = False
                    mainMenu()
        screen.blit(Win, (0, 0))
        font = pygame.font.Font('freesansbold.ttf', 60)
        # Draws a rectangle that has text inside it
        text = font.render("YOU WIN", True, YELLOW)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH / 2, 250)
        screen.blit(text, textRect)  # Puts the textbox on the screen

        font = pygame.font.Font('freesansbold.ttf', 30)
        text2 = font.render("press Q to exit to main menu", True, GREEN)
        textRect2 = text.get_rect()
        textRect2.center = (210, 350)
        screen.blit(text2, textRect2)

        dis_score = font.render("Final Score: " + str(score), True, YELLOW)
        screen.blit(dis_score, (225, 400))

        pygame.display.update()
    screen.fill(bgColour)
    pygame.display.update()


mainMenu()
bricks()
#<------MAIN GAME LOOP------>
while running:
    #Keybinds that quit the game or pause the game
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            running = False
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_p):
            pause()

    drawBall(ballX, ballY, bgColour)
    drawRect(rectX, rectY, bgColour)
    #Controlling the paddle
    keys = pygame.key.get_pressed()
    #How many pixels the paddle moves
    paddleSpeed = 3
    if (keys[pygame.K_LEFT]):
        if (rectX > 0):
            rectX -= paddleSpeed

    if (keys[pygame.K_RIGHT]):
        if (rectX + 100 < SCREEN_WIDTH):
            rectX += paddleSpeed
    #Ball collision with screen borders
    ballX += dx
    ballY += dy
    #Checks which wall the ball collides with and changes the direction appropriately
    if ballX < ballRadius:
        dx = randNumPositive
    elif ballX > SCREEN_WIDTH - ballRadius:
        dx = randNumNegative
    elif ballY < ballRadius:
        dy = randNumPositive
    elif ballY > SCREEN_HEIGHT - ballRadius:
        #When ball hits border beneath paddle, decreases lives by 1
        dy = randNumNegative
        lives -= 1
        #When no lives are left, displays game over screen and resets lives and score, and redraws ball and rectangle in original positions
        if (lives == 0):
            gameOver()
            bricks()
            ballX = 200
            ballY = 300
            rectX = SCREEN_WIDTH - 350
            rectY = SCREEN_HEIGHT - 50
            dx = 1
            dy = 1
            drawBall(ballX, ballY, WHITE)
            drawRect(rectX, rectY, GREEN)
            score = 0
            lives = 3
    #If ball collides with paddle, changes direction depending on which half of the screen the ball is in
    if (pygame.Rect.colliderect(ball, myRect)):
        dy = randNumNegative
        if (dx > 0):
            dx = randNumPositive
        elif (dx < 0):
            dx = randNumNegative
    #If ball collides with any of the bricks in the list, changes direction appropriately
    for brick in brickList.copy():
        if ball.colliderect(brick):
            #If ball collides with a brick, increases score by one
            score += 1
            #If ball collides with a brick, removes that brick from list and redraws it in background colour
            brickList.remove(brick)
            pygame.draw.rect(screen, bgColour, brick)
            #If all bricks are broken
            if (len(brickList) == 0):
                #If all bricks on the screen are broken and removed from list, displays win screen and resets lives and score, and redraws ball and rectangle in original positions
                winScreen()
                bricks()
                dx = 1
                dy = -1
                ballX = 200
                ballY = 300
                rectX = SCREEN_WIDTH - 350
                rectY = SCREEN_HEIGHT - 50
                drawBall(ballX, ballY, WHITE)
                drawRect(rectX, rectY, GREEN)
                score = 0
                lives = 3
            #Checks if ball hits the bottom or the top of a brick and changes direction appropriately
            if (dy < 0):
                dy = randNumPositive
            elif (dy > 0):
                dy = randNumNegative
            if (dx > 0):
                dx = randNumPositive
            elif (dx < 0):
                dx = randNumNegative
    #Text box for displaying score
    font = pygame.font.Font(None, 30)
    dis_score = font.render("Score: " + str(score), True, YELLOW)
    screen.fill(bgColour, (500, SCREEN_HEIGHT - 595, 120, 30))
    screen.blit(dis_score, (500, SCREEN_HEIGHT - 595))
    #Text box for displaying lives
    dis_live = font.render("Lives: " + str(lives), True, YELLOW)
    screen.fill(bgColour, (0, SCREEN_HEIGHT - 595, 120, 30))
    screen.blit(dis_live, (10, SCREEN_HEIGHT - 595))
    #Redrawing ball and paddle so they are visible on screen
    drawBall(ballX, ballY, WHITE)
    drawRect(rectX, rectY, GREEN)
    pygame.display.update()
    #Forcing the game to run at set speed
    fpsClock.tick(FPS)
pygame.quit()
pygame.display.flip()
