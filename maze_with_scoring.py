# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "Coin Hunt"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Sounds
pygame.mixer.music.load("upbeat.ogg")
splash = pygame.image.load('splash.jpg')
pygame.mixer.music.play(-1) 

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Fonts
MY_FONT = pygame.font.Font(None, 50)

# stages
START = 0
PLAYING = 1
END = 2


# make walls
h_wall1 =  [300, 275, 200, 25]
h_wall2 =  [400, 450, 200, 25]
v_wall3 =  [100, 100, 25, 200]
v_wall4 =  [200, 400, 25, 200]
h_wall5 =  [600, 650, 200, 25]
h_wall6 =  [850, 575, 200, 25]
h_wall7 =  [850, 475, 200, 25]
h_wall8 =  [850, 375, 200, 25]
h_wall9 =  [850, 275, 200, 25]
h_wall10 = [850, 175, 200, 25]
h_wall11 = [850, 75, 200, 25]
h_wall12 = [850, 675, 200, 25]
v_wall13 =  [200, -20, 25, 200]
v_wall14 =  [300, -20, 25, 200]

walls = [h_wall1, h_wall2, v_wall3, v_wall4, h_wall5,
         h_wall6, h_wall7, h_wall8, h_wall9, h_wall10,
         h_wall11, h_wall12, v_wall13, v_wall14]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]  
coin3 = [150, 150, 25, 25]
coin4 = [650, 400, 25, 25]
coin5 = [750, 300, 25, 25]
coin6 = [450, 100, 25, 25]
coin7 = [575, 600, 25, 25]
coin8 = [50, 600, 25, 25]
coin9 = [500, 60, 25, 25]

def setup():
    global stage, time_remaining, ticks, player1, vel1, player1_speed, score1, coins, win, lose
    
    stage = START
    time_remaining = 10
    ticks = 0

    # Make a player
    player1 =  [25, 25, 25, 25]
    vel1 = [0, 0]
    player1_speed = 5
    score1 = 0
    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9]
    win = False
    lose = False

# Game loop
done = False

setup()
while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if stage == START:
                if event.key == pygame.K_SPACE:
                    print("Go")
                    stage = PLAYING
                    
            elif stage == PLAYING:
                pass

            elif stage == END:
                pass

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()
        
        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if left:
            vel1[0] = -player1_speed
        elif right:
            vel1[0] = player1_speed
        else:
            vel1[0] = 0

        if up:
            vel1[1] = -player1_speed
        elif down:
            vel1[1] = player1_speed
        else:
            vel1[1] = 0
        
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''        
    if stage == PLAYING:
        player1[0] += vel1[0]

        ''' resolve collisions horizontally '''
        for w in walls:
            if intersects.rect_rect(player1, w):        
                if vel1[0] > 0:
                    player1[0] = w[0] - player1[2]
                elif vel1[0] < 0:
                    player1[0] = w[0] + w[2]

        ''' move the player in vertical direction '''
        player1[1] += vel1[1]
        
        ''' resolve collisions vertically '''
        for w in walls:
            if intersects.rect_rect(player1, w):                    
                if vel1[1] > 0:
                    player1[1] = w[1] - player1[3]
                if vel1[1]< 0:
                    player1[1] = w[1] + w[3]

        ''' here is where you should resolve player collisions with screen edges '''




        ''' get the coins '''
        hit_list = []

        for c in coins:
            if intersects.rect_rect(player1, c):
                hit_list.append(c)
         
        hit_list = [c for c in coins if intersects.rect_rect(player1, c)]
        
        for hit in hit_list:
            coins.remove(hit)
            score1 += 1
            print("sound!")
            
        if len(coins) == 0:
            win = True
            
        elif len(coins) == 0:
            lose = True
        
        ''' timer stuff '''
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    
    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [50, 50])
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if stage == START:
        
        screen.blit(splash, [0, 0])
        text1 = MY_FONT.render("Coin Hunt!", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to start.)", True, WHITE)
        screen.blit(text1, [400, 400])
        screen.blit(text2, [300, 450])
        
    if win:
        font = pygame.font.Font(None, 100)
        text = font.render("You Win!", 1, WHITE)
        screen.blit(text, [450, 500])

    if lose:
        font = pygame.font.Font(None, 48)
        text = font.render("You lose!", 1, GREEN)
        screen.blit(text, [400, 200])
        
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
