##
## Author: Kristina Striegnitz and Daniel W. Wolf
##
## 10-31-2013
##
## shooting-monsters-task4
##
## This program shows a player character (orange ball) which can be
## controlled using the 'a'and 'd' keys. It also displays a score.
##

#import the modules 
import pygame
import random
import math

RADIUS = 0
X = 1
Y = 2
XVEL = 3
YVEL = 4
COLOR = 5
COLLIDED = 6
#function that makes the enemies
def make_ball(width, height):
   radius = 20
   x= random.randint(radius, width-radius)
   y = radius
   xvel = 2
   yvel = 0
   color = (0,240,0)
   ball = [radius, x, y, xvel, yvel, color]
   return ball


#function that makes the fireballs
def make_fireball(x,y):
    radius = 6
    xvel=0
    yvel=-8
    collided=False
    color = (240,0,0)
    fireball = [radius,x,y,xvel,yvel,color,collided]
    return fireball
    
    

def distance (x1, y1, x2, y2):
    """Calculates the distance between two points (x1, y1) and
    (x2,y2)."""
    
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#function for filtering the fireballs when they leave the window
def filter_fireballs(fireballs):
    newlist=[]
    for element in fireballs:
        if element[Y]>0:
            newlist+=[element]
    return newlist
    
        

def run_game():
    
    ## Initialize the pygame submodules and set up the display window.
    pygame.init()

    width = 640
    height = 480
    my_win = pygame.display.set_mode((width,height))

    myFont = pygame.font.Font(None,30)
    fireballs=[]
    balls=[]

   #handle making 5 enemies
    count=1

    while count<6:

        ball = make_ball(width,height)

        balls+=[ball]

        count+=1
    

    # starting position, size, and velocity for the player character
    radius = 20
    x = random.randint(radius, width-radius)
    y = height - radius
    xvel = 0


    score = 0
    
    
    # boolean variables to capture player input
    up = False
    down = False
    left = False
    right = False
    shoot = False
    ## The game loop starts here.

            
    clock= pygame.time.Clock()
    keepGoing = True    
    while (keepGoing):

        ## Handle events.
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == "a":
                    left = True
                elif pygame.key.name(event.key) == "d":
                    right = True
                if pygame.key.name(event.key) == "space":
                    shoot =True
            elif event.type == pygame.KEYUP:
                if pygame.key.name(event.key) == "a":
                    left = False
                elif pygame.key.name(event.key) == "d":
                    right = False
                if pygame.key.name(event.key) == "space":
                    shoot = False
                    
                    
                
        clock.tick(60)


        #update the enemies position       
        for ball in balls:
            ball[X] = ball[X] + ball[XVEL]
        for fireball in fireballs:
            fireball[Y] = fireball[Y] + fireball[YVEL]


            
        
        # make sure enemies stay inside pygame window and update enemy
        # velocity
        for ball in balls:
            if (ball[X] < ball[RADIUS]):
                ball[X] = ball[RADIUS]
                ball[XVEL] = -1 * ball[XVEL]
            elif (ball[X] > width - ball[RADIUS]):
                ball[X] = width - ball[RADIUS]
                ball[XVEL] = -1 * ball[XVEL]
            if (ball[Y] < ball[RADIUS]):
                ball[Y] = ball[RADIUS]
                ball[YVEL] = -1 * ball[YVEL]
            if (ball[Y] > height - ball[RADIUS]):
                ball[Y] = height - ball[RADIUS]
                ball[YVEL] = -1 * ball[YVEL]

                
        ## Simulate game world
        # update velocity according to player input
        if left and not right:
            xvel = -6
        elif right and not left:
            xvel = 6
        else:
            xvel = 0
        #handle firing the lasers
        if shoot == True:
            
            fireball = make_fireball(x,y)
            fireballs+=[fireball]
            if shoot == True:
               shoot = False
        #handle collision detection
        for fireball in fireballs:
           for ball in balls:
              if fireball[COLLIDED]==False:    
                 if distance(fireball[X],fireball[Y], ball[X], ball[Y]) <= ball[RADIUS]:
                    print "hit!"
                    score+=1
                    fireball[COLLIDED]=True
                 
                
        # move player character
        x = x + xvel

            
        ## Draw picture and update display
        my_win.fill(pygame.color.Color("black"))

        for fireball in fireballs:
            position = ((fireball[X]),(fireball[Y]))
            pygame.draw.circle(my_win, fireball[COLOR], position, fireball[RADIUS])
            

        for ball in balls:
            position = ((ball[X]),(ball[Y]))
            pygame.draw.circle(my_win, ball[COLOR], position, ball[RADIUS])

        
        
        msg = myFont.render("Your score: "+str(score), True, pygame.color.Color("magenta"))
        my_win.blit(msg, (20,height-40)) 
        pygame.draw.circle(my_win, pygame.color.Color('orange'), (x,y), radius)
         
        
         
        #filter out the fireballs that haveleft the screen
        fireballs= filter_fireballs(fireballs)
        print fireballs
        
        pygame.display.update()
        
      
        
    ## The game loop ends here.

    pygame.quit()


## Call the function run_game.

run_game()
