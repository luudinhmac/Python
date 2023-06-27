import pygame
from random import randint


def covid_move(covid_frame_list):
    if covid_frame_list:
        for covid_rect in covid_frame_list:
            covid_rect.x -= 5
            screen.blit(covid_surf, covid_rect)
        # Remove covid out side of screen    
        for covid in covid_frame_list:
            if covid.left <=-100:
                covid_frame_list.remove(covid)  

def collision_covid(player_frame, covide_frame_list):
    if covid_frame_list:
        for covid_rect in covid_frame_list:
            if player_frame.colliderect(covid_rect):
                return False
    return True


pygame.init()  # init all modules pygame was imported, call it at first position
screen = pygame.display.set_mode((800, 400))  # init module show(width, high)
pygame.display.set_caption("CovidFighting")
clock = pygame.time.Clock()

bautroi_surface = pygame.image.load(
    "game/graphics/300.png").convert_alpha()  # load image sky
matdat_surface = pygame.image.load(
    "game/graphics/100.png").convert_alpha()  # load image playground

# add player
player_walk = pygame.image.load(
    "game/graphics/Player/rsz_1doctor_walk_e1.png").convert_alpha()  # load player image
player_jump = pygame.image.load(
    "game/graphics/Player/doctor_jum.png").convert_alpha()  # load player image

player_surface = player_walk
# create frame for object
player_frame = player_surface.get_rect(midbottom=(70, 300))
# about
play_stand = pygame.image.load(
    "game/graphics/Player/rsz_intro.png").convert_alpha()
play_stand_frame = play_stand.get_rect(center=(400, 200))

# font
font = pygame.font.Font("game/font/UVNButLong2.TTF", 30)
game_name = font.render("Covid fighting 2023", True, (255, 20, 147))
game_name_frame = game_name.get_rect(center=(126, 50))

# continue play
game_hd = font.render("Press SPACE to play", True, (25, 25, 122))
game_hd_frame = game_hd.get_rect(center=(400, 370))
# add covid
covid_surf = pygame.image.load(
    'game/graphics/covid/rsz_covid1.png').convert_alpha()
covid_frame = covid_surf.get_rect(midbottom=(700, 250))
covid_frame_list = []
# Time covid show
covid_timer = pygame.USEREVENT + 1
pygame.time.set_timer(covid_timer, 1500)
# add gravision
player_grav = 0
game_active = False

bg_music = pygame.mixer.Sound("game/audio/music.wav")
bg_music.play(loops=-1)
bg_music.set_volume(0.2)

while True:
    # Create button exit when click x on the window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_frame.bottom >= 300:
                    player_grav = -20
                    jump_sound = pygame.mixer.Sound("game/audio/jump.mp3")
                    jump_sound.play()
            # if event.type == pygame.KEYUP:
            #     pass
            if event.type == covid_timer:
                covid_frame_list.append(covid_surf.get_rect(
                    bottomright=(randint(900, 1100), 280)))
                print(covid_frame_list)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                covid_frame.left = 800
    if game_active:
        screen.blit(bautroi_surface, (0, 0))  # set up sky image
        screen.blit(matdat_surface, (0, 300))  # setup playground image
        # player
        if player_frame.bottom < 300:
            player_surface = player_jump
        else:
            player_surface = player_walk
        player_grav += 1
        player_frame.y += player_grav
        if player_frame.bottom >= 300:
            player_frame.bottom = 300
        screen.blit(player_surface, player_frame)  # setup player image
        covid_move(covid_frame_list)
        game_active= collision_covid(player_frame,covid_frame_list) #
        # screen.blit(covid_surf, covid_frame)
        # covid_frame.x -= 5

        # if covid_frame.left <= -100:
        #     covid_frame.left = 800

        # if covid_frame.colliderect(player_frame):
        #     game_active = False
    else:
        screen.fill((224, 255, 255))
        screen.blit(play_stand, play_stand_frame)
        screen.blit(game_name, game_name_frame)
        screen.blit(game_hd, game_hd_frame)
        covid_frame_list.clear()
    pygame.display.update()
    clock.tick(60)
