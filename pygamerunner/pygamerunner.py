# cd "C:\Users\ABID_\OneDrive\Desktop\pygamerunner"
import pygame 
from sys import exit

# initialise pygame
pygame.init() 
running = True

# screen size
screen = pygame.display.set_mode((800,400))

# window caption and icon
pygame.display.set_caption('PyGame Runner')
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
icon_surface = pygame.image.load('graphics/run_icon.png').convert_alpha()
pygame.display.set_icon(icon_surface)

# FPS 
clock = pygame.time.Clock()

# background surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('PyRunner',False,'black').convert()

score = 67
score_surface = test_font.render(f'Score: {score}',False,'black').convert()
score_rect = score_surface.get_rect(center = (400,50))

# sprites surfaces
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (750,300))
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50,300))
player_gravity = 0

while running:
    # for event = closing the game tab
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                player_gravity = -20

        if event.type == pygame.KEYUP:
            print('key up')

    # background surface + text
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))    
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    screen.blit(text_surface,(20,20))
    screen.blit(score_surface,score_rect)

    # player animations/coordinates 
    player_rect.y += player_gravity
    screen.blit(player_surf,player_rect)

    
    # snail animations/coordinates
    screen.blit(snail_surface,snail_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0: 
        snail_rect.left = 800
        score += 1

    # collisions
    player_rect.colliderect(snail_rect)

    # mouse colision checker
    mouse_pos = pygame.mouse.get_pos()

    pygame.display.update()
    clock.tick(60)