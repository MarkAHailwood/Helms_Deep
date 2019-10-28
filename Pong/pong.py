# import the pygame library and initialise the game engine
import pygame
pygame.init()
#import the paddle class that we imported
from paddle import Paddle
from ball import Ball

#define the colours to use in the game
BLACK = (0,0,0)
WHITE = (255,255,255)     
    
#define the size of, open, and set the title of a new window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My_First_Joll : Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 5
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 685
paddleB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

#This will be the list of all sprites we use in our game
all_sprites_list = pygame.sprite.Group()

#add the young paddles to this list
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)


#set the main program loop - the key part of the game - it has 3 parts
#Part 1 : capturing events - used to listen to user inputs and react (Key strokes or mouse movements)
#Part 2 : Implement the game logic ie. What happens when the code is run
#Part 3 : Refresh the screen by redrawing the stage and sprites, when needs be

#Make the loop continue until user exits the game
carryOn = True

#Use the clock to contrl how fast the screen updates
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0

#------Main Program Loop--------#
while carryOn:
        #main event loop
        for event in pygame.event.get():#when user does something
            if event.type == pygame.QUIT: #if user clicks close
                carryOn = False #the loop ends
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #when x pressed
                        carryOn=False

        #moving the paddles when using arrows or W/S
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(5)
        if keys[pygame.K_s]:
            paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(5)
                        

        #game logic
        all_sprites_list.update()

        #check if the ball is bouncing against any of the walls
        if ball.rect.x>=690:
            scoreA+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB+=1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1]   

        #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
          ball.bounce()
        
        #drawing code here
        #step 1 : clear the screen to black
        screen.fill(BLACK)
        #draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        #draw all the sprites in one go
        all_sprites_list.draw(screen)

        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (250,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (420,10))
 

        #update the screen with what we have drawn
        pygame.display.flip()

        #limit the screen refresh to 60 frames per second
        clock.tick(60)

#Once we exit the main program loop we can stop the game
pygame.quit()

        
