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

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


# Make a player
player1 =  [200, 150, 25, 25]
vel1 = [0, 0]
player1_speed = 5
score1 = 0

# make walls
h_wall1 =  [300, 275, 200, 25]
h_wall2 =  [400, 450, 200, 25]
v_wall3 =  [100, 100, 25, 200]
v_wall4 =  [200, 400, 25, 200]
h_wall5 =  [600, 650, 200, 25]
h_wall6 =  [850, 575, 200, 25]
h_wall7 =  [850, 475, 200, 25]
h_wall8 =  [850, 375, 200, 25]

walls = [h_wall1, h_wall2, v_wall3, v_wall4, h_wall5, h_wall6, h_wall7, h_wall8]

# Make coins
coin1 = [300, 500, 25, 25]
coin2 = [400, 200, 25, 25]
coin3 = [150, 150, 25, 25]
coin4 = [650, 300, 25, 25]

coins = [coin1, coin2, coin3, coin4]


# Game loop
win = False
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

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

        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    
    for w in walls:
        pygame.draw.rect(screen, RED, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    if win:
        font = pygame.font.Font(None, 48)
        text = font.render("You Win!", 1, GREEN)
        screen.blit(text, [400, 200])

    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
