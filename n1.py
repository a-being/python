import sys,pygame
import time
import random

#help
#random.randrange(0, 100)
#mouse = pygame.mouse.get_pos()
# mouse[0], mouse[1]

#click = pygame.mouse.get_pressed()
# click[0] == 1




#constants variables
white = (255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
colors=[white,black,blue,green,red]
tot_colors=len(colors)
#global funcs

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text,scr,display_width,display_height):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    scr.blit(TextSurf, TextRect)
    #pygame.display.update()


def game1():
    #initize
    display_width = 800
    display_height = 600
    bgcolor=0
    
    
    #code
    pygame.init()
    scr = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()
    stopGame = False
    
    while not stopGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopGame=True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0    
    
        scr.fill(colors[bgcolor])
        bgcolor=bgcolor+1
        if bgcolor ==tot_colors: 
           bgcolor=0
        message_display("dasdsad",scr,display_width,display_height)         
        pygame.display.update()
        clock.tick(20)

def game2():
    #initize
    display_width = 800
    display_height = 600
    bgcolor=0
    noOfCircles=4
    scircle=1
    startRadius = 50
    circleWidth = 5
    x=display_width/2
    y=display_height/2
        
    #code
    pygame.init()
    scr = pygame.display.set_mode((display_width,display_height))
    
    pygame.display.set_caption('A bit Racey')
    #clock = pygame.time.Clock()
    stopGame = False
    scr.fill(colors[bgcolor]) #white color 
    while not stopGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopGame=True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0    
        startCircle = scircle
        for i in range(noOfCircles):
            rad = (i*circleWidth)+startRadius
            
            if (startCircle == 1):
               pygame.draw.circle(scr,colors[1],(x,y),rad,circleWidth,draw_top_right=True)
               
            if (startCircle == 2):
               pygame.draw.circle(scr,colors[2],(x,y),rad,circleWidth,draw_bottom_right=True)
            if (startCircle == 3):
               pygame.draw.circle(scr,colors[3],(x,y),rad,circleWidth,draw_bottom_left=True)
            if (startCircle == 4):
               pygame.draw.circle(scr,colors[4],(x,y),rad,circleWidth,draw_top_left=True)
            
            pygame.display.update()
            
            
            
            startCircle+=1
            if startCircle >=5:
               startCircle=1
        scircle+=1   
        time.sleep(4)        
               
def game3():
    #initize
    display_width = 800
    display_height = 600
    bgcolor=0
    
    
    rad = 65
    circleWidth = 20
    x=display_width/2
    y=display_height/2
    

    c1=black 
    c2=blue
    c3=green
    c4=red
        
    #code
    pygame.init()
    scr = pygame.display.set_mode((display_width,display_height))
    
    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()
    stopGame = False
    scr.fill(colors[bgcolor]) #white color 
    
    while not stopGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopGame=True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0    
        
            
            
        pygame.draw.circle(scr,c1,(x,y),rad,circleWidth,draw_top_right=True)
        
        pygame.draw.circle(scr,c2,(x,y),rad,circleWidth,draw_bottom_right=True)
    
        pygame.draw.circle(scr,c3,(x,y),rad,circleWidth,draw_bottom_left=True)
    
        pygame.draw.circle(scr,c4,(x,y),rad,circleWidth,draw_top_left=True)
    
        aaa=c4
        c4=c3
        c3=c2
        c2=c1 
        c1=aaa 
         
        
        pygame.display.update()
          
        #time.sleep(0.2)        
            
    

        #pygame.display.update()
        clock.tick(1)
           
    
# Main code
#=====================================

game3()
pygame.quit()
#quit()

    