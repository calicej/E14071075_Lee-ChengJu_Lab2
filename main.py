import pygame
import math

# for timer：存取時間
start_ticks = pygame.time.get_ticks()
# setup
WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()
# create window surface
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
# set window caption
pygame.display.set_caption("My first game")
# clock
clock = pygame.time.Clock()

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("images/enemy.png"), (BTN_WIDTH, BTN_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("images/muse.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("images/sound.png"), (BTN_WIDTH, BTN_HEIGHT))
continue_image = pygame.transform.scale(pygame.image.load("images/continue.png"), (BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("images/pause.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("images/hp.png"), (50, 50))
hp_gray_image = pygame.transform.scale(pygame.image.load("images/hp_gray.png"), (50, 50))

run = True
# game loop
while run:
    clock.tick(FPS)
    # event loop (user action)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # draw background
    window.blit(background_image, (0, 0))
    # draw enemy
    window.blit(enemy_image, (38, 200))
    # draw health bar
    pygame.draw.rect(window, RED, [40, 180, 80, 10])
    # draw menu
    pygame.draw.rect(window, BLACK, [0, 0, WIN_WIDTH, 85])
    # draw buttons
    window.blit(muse_image, (730, 8))
    window.blit(sound_image, (800, 8))
    window.blit(continue_image, (870, 8))
    window.blit(pause_image, (940, 8))
    # draw timer_background
    pygame.draw.rect(window, BLACK, [0, WIN_HEIGHT-65, 110, 65])
    # draw hp：有兩行，用兩個 for 迴圈來分別擺放綠色及灰色的 hp
    for i in range(5):
        window.blit(hp_gray_image, (380 + i * 50, 0.8))
    for i in range(5):
        window.blit(hp_gray_image, (380 + i * 50, 40))
    for i in range(5):
        window.blit(hp_image, (380 + i * 50, 0.8))
    for i in range(2):
        window.blit(hp_image, (380 + i * 50, 40))

    # 抓取現在時間 - 開始時間 = 經過的時間
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    # 把秒數換成分鐘數，並取其商數；將值存入 str，並限制顯示兩位數，不足者補零
    mins = str(math.floor(seconds) // 60).rjust(2, '0')
    # 把秒數換成分鐘數，並取其餘數；將值存入 str，並限制顯示兩位數，不足者補零
    secs = str(math.floor(seconds) % 60).rjust(2, '0')
    # 設定 timer 輸出的字體大小
    font = pygame.font.SysFont(None, 48)
    # 輸出 timer，格式為「分鐘：秒鐘」
    text_surface = font.render(mins + ':' + secs, True, WHITE)
    window.blit(text_surface, (10, WIN_HEIGHT-50))

    pygame.display.update()



# uninitialize all the pygame module
pygame.quit()

