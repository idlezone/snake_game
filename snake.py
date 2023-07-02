import pygame
import time
from random import random
pygame.init()
screen = pygame.display.set_mode([600,600])
running = True
# x = 300
# y = 300
snake=[]
timer = time.time()
food_x= int(600*random()/20)*20
food_y= int(600*random()/20)*20
head = pygame.Rect(300,300,20,20)
snake.append(head)
direction = [0]
while running:
   
    # generate food
    if time.time()-timer > 6:
        food_x= int(600*random()/20)*20
        food_y= int(600*random()/20)*20
        timer+=6
        food = pygame.Rect(food_x,food_y,20,20)
        pygame.draw.rect(screen,(0,255,255),food)

    # snake automatic moves
    for i in range(len(direction)):
        if direction[i] ==0:
            snake[i][1]+=20
        if direction[i] ==1:
            snake[i][0]+=20
        if direction[i] ==2:
            snake[i][1]-=20
        if direction[i] ==3:
            snake[i][0]-=20

    # update direction based on part ahead 
    for i in range(len(direction)):
        if i!=0:
            direction[i]=direction[i-1]

    #events triggered by keyboard       
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # y-=20
            # print("Down") 
            if event.key == pygame.K_DOWN:
                dir=2
                for body in snake:
                    body[1]+=20
                    
            if event.key == pygame.K_UP:
                dir=0
                for body in snake:
                    body[1]-=20
            if event.key == pygame.K_LEFT:
                dir=3
                for body in snake:
                    body[0]-=20
            if event.key == pygame.K_RIGHT:
                dir=1
                for body in snake:
                    body[0]+=20
            direction[0]=dir
    
    #eat food
    if food_x == snake[0][0] and food_y == snake[0][1]:
        snake.append([snake[0][0],snake[0][1]])
        direction.append(direction[len(direction)-1])
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,0,255),head)

    # draw the snake
    for part in snake:
        pygame.draw.rect(screen,(0,0,255),pygame.Rect(part[0],part[1],20,20))


    # font=pygame.font.SysFont("Arial",36)
    # txtsurf=font.render(str(y),True,(255,255,255))
    # txtsurf=font.render(str(y).encode("utf-8").decode("utf-8"),True,(255,255,255))

    # screen.blit(txtsurf,(200-txtsurf.get_width()//2, 150-txtsurf.get_height()//2))
    # screen.blit(txtsurf,(200, 200))

    pygame.display.update()
    # x+=20
    # y+=1
    snake[0][0]=snake[0][0] % 600
    snake[0][1]=snake[0][1] % 600
    # time.sleep(0.1)
    
pygame.quit()