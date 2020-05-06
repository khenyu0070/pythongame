import pygame, random
import time

pygame.font.get_fonts()

pygame.init()



background = (38,13, 14)
white = (255,255,255)
green = (77,237,48)

X=400
Y=800
speed=0.003
point=0

red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)


win = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Typing Game")
clock = pygame.time.Clock()



def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((X/2),(Y/2))
    win.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

  
    
def gameover():
    message_display('Game Over')

       
font = pygame.font.SysFont("ComicSansMs", 32)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
        

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(win, ac,(x,y,w,h))
        if click[0] == 1:
            if action == "play":
                print('clicked')
                new_word()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(win, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    win.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        win.fill(background)
        largeText = pygame.font.Font('freesansbold.ttf',32)
        TextSurf, TextRect = text_objects("Typing Game", largeText)
        TextRect.center = ((X/2),(Y/2))
        win.blit(TextSurf, TextRect)

        button("Start",150,450,100,50,green,bright_green,"play")
        button("Quit",150,520,100,50,red,bright_red,"quit")
        
                
        pygame.display.update()
        clock.tick(15)   


def new_word():
    
    global chosenWord, pressedWord, word_X, word_Y, text, pointCaption, speed, gameover
    word_X = random.randint(100, 300)
    word_Y = 0
    speed += 0.02
    pressedWord = ""
    lines = open("ranwords.txt").read().splitlines()
    chosenWord = random.choice(lines)
    text = font.render(chosenWord, True, white)


new_word()

while True:
        
    
    win.fill(background)
    
    word_Y += speed
    
    win.blit(text,(word_X, word_Y))
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                pressedWord += pygame.key.name(event.key)
                if chosenWord.startswith(pressedWord):
                    if chosenWord == pressedWord:
                        point += len(chosenWord)
                        new_word()
                else:
                    pressedWord = ""
    pointCaption = font.render('Score:' + str(point), True,green)
    win.blit(pointCaption,(10,5))
    
    if word_Y < Y-5:
        pygame.display.update()
      
    else:
        
        speed = 0.02
        point = 0
        new_word()
        gameover()
       
            






pygame.quit()
quit()

        
