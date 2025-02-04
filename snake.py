import pygame
import time
from random import random
DIMENSION = 400

def boundary(a):
    if a>= DIMENSION:
        return DIMENSION-20
    if a<0:
        return 0
    return a

pygame.init()
screen = pygame.display.set_mode([DIMENSION,DIMENSION])
running = True
snake = []
food_timer = time.time()
snake_timer= time.time()
food_x= int(DIMENSION*random()/20)*20
food_y= int(DIMENSION*random()/20)*20
# head = pygame.Rect(DIMENSION/2,DIMENSION/2,20,20)
snake.append([DIMENSION/20,DIMENSION/20])
# for i in range(len(snake)-1):
#     snake_latter[i+1] = snake[i]
direction = [0]
while running:
    screen.fill((0,0,0))
    point=0
    # generate food every 6s
    if time.time()-food_timer > 12:
        food_x= int(DIMENSION*random()/20)*20
        food_y= int(DIMENSION*random()/20)*20
        food_timer+=12
    food = pygame.Rect(food_x,food_y,20,20)
    pygame.draw.rect(screen,(0,255,255),food)
   
    
    # snake automatic moves
    if time.time()-snake_timer > 0.5:
        for i in range(len(direction)):
            if direction[i] ==0:
                snake[i][1]-=20
                snake[i][1]=boundary(snake[i][1])
            if direction[i] ==1:
                snake[i][0]+=20
                snake[i][0]=boundary(snake[i][0])
            if direction[i] ==2:
                snake[i][1]+=20
                snake[i][1]=boundary(snake[i][1])
            if direction[i] ==3:
                snake[i][0]-=20
                snake[i][0]=boundary(snake[i][0])
        snake_timer+=0.5
        
    # update direction based on part ahead 
    for i in range(len(direction)-1):
        # if i!=0:
        direction[len(snake)-i-1] = direction[len(snake)-i-2]
    # for i in range(len(snake)):
        # if i!=0:
            # snake_latter[i] = snake[i-1]
            # put it in the keyboard loop

    #events triggered by keyboard 
    # T=0.5
    # key_timer=time.time()
    for event in pygame.event.get():
        print(snake)
        if event.type ==pygame.QUIT:
            running = False
        # key_timer=time.time()
        if event.type == pygame.KEYDOWN:
            # for i in range(len(snake)-1):
            #     snake_latter[i+1] = snake[i]
            
            # y-=20
            # print("Down") 
            if event.key == pygame.K_DOWN:
                dir=2
                # for part in snake:
                    # part[1] += 20
                for i in range(len(snake)-1):
                    snake[len(snake)-i-1] = snake[len(snake)-i-2]
                
                snake[0][1] += 20
                snake[0][1] = boundary(snake[0][1])
               
                    # part = part
                # for i in range
                #     snake[i+1] = snake[i]
                #     body[1]+=20
                # if time.time()-key_timer > 0.5:
                   
                # for j in range(len(snake)):
                #     if direction[0]==2 or direction[0]==0:
                #         continue
                #     if direction[0]==1 or direction[0]==3:
                #         snake[0][1]+=20
                    #     for i in range(len(direction)):
                    #         # if time.time()-key_timer > 0.5:
                    #         if i!=0:
                    #             direction[i]=direction[i-1]
                    # # key_timer+=0.5

            if event.key == pygame.K_UP:
                dir=0
                # for part in snake:
                for i in range(len(snake)-1):
                    snake[len(snake)-i-1] = snake[len(snake)-i-2]
                snake[0][1] -= 20
                snake[0][1] = boundary(snake[0][1])
                    # part[1] -= 20
                    # part = part
                    # snake[i+1] = snake[i]
                    # part[1] = boundary(part[1])
                
            if event.key == pygame.K_LEFT:
                dir=3
                # for part in snake:
                for i in range(len(snake)-1):
                    snake[len(snake)-i-1] = snake[len(snake)-i-2]
                snake[0][0] -= 20
                snake[0][0]= boundary(snake[0][0])
                    # part[0] -= 20
                    # part = part
                    # snake[i+1] = snake[i]
                    # part[0] = boundary(part[0])
                # for i in range(len(snake)-1):
                #     snake[i+1] = snake_latter[i+1]
                
            if event.key == pygame.K_RIGHT:
                dir=1
                # for part in snake:
                for i in range(len(snake)-1):
                    snake[len(snake)-i-1] = snake[len(snake)-i-2]
                snake[0][0] += 20
                snake[0][0] = boundary(snake[0][0])
                    # part[0] += 20
                    # part = part
                    # snake[i+1] = snake[i]
                    # part[0] = boundary(part[0])
                
                # for i in range(len(snake)-1):
                    # snake[i+1] = snake_latter[i+1]


            direction[0] = dir
            # if time.time()-key_timer > 0.5:

    #eat food
    if food_x == snake[0][0] and food_y == snake[0][1]:
        if time.time()-snake_timer < 0.5:

            l = len(snake)
        # snake.append([snake[len(snake)-1][0],snake[len(snake)-1][1]])
        # snake.append([snake[l-1][0],snake[l-1][1]])
        # snake.append([])
        # new_l = l
            if direction[len(direction)-1] == 0:
                snake[l-1][1]-=20
                snake.append([snake[l-1][0],snake[l-1][1]+20])
            if direction[len(direction)-1] == 1:
                snake[l-1][0]+=20
                snake.append([snake[l-1][0]-20,snake[l-1][1]])
            if direction[len(direction)-1] == 2:
                snake[l-1][1]+=20
                snake.append([snake[l-1][0],snake[l-1][1]-20])
            if direction[len(direction)-1] == 3:
                snake[l-1][0]-=20
                snake.append([snake[l-1][0]+20,snake[l-1][1]])

        direction.append(direction[len(direction)-1])
        food_x = int(DIMENSION*random()/20)*20
        food_y = int(DIMENSION*random()/20)*20
        
        # if new_l == l+20:
        #     point+=10
        # print("current score :",point)
            # print("current score :",point)

    # draw the snake
    for i in range(len(snake)):
        if i==0:
            pygame.draw.rect(screen,(255,0,0),pygame.Rect(snake[0][0],snake[0][1],20,20))
        else:
            pygame.draw.rect(screen,(0,0,255),pygame.Rect(snake[i][0],snake[i][1],20,20))
    # record the point

    # font=pygame.font.SysFont("Arial",36)
    # txtsurf=font.render(str(y),True,(255,255,255))
    # txtsurf=font.render(str(y).encode("utf-8").decode("utf-8"),True,(255,255,255))

    # screen.blit(txtsurf,(200-txtsurf.get_width()//2, 150-txtsurf.get_height()//2))
    # screen.blit(txtsurf,(200, 200))

    pygame.display.update()
    # x+=20
    # y+=1
    # snake[0][0]=snake[0][0] % DIMENSION
    # snake[0][1]=snake[0][1] % DIMENSION
    # time.sleep(0.1)
    
pygame.quit()
    
