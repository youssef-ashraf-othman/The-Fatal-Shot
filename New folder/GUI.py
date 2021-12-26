import pygame
pygame.init()
pygame.font.init()
move_right = [pygame.image.load("hero/R1.png"), pygame.image.load("hero/R2.png"), pygame.image.load("hero/R3.png"),
              pygame.image.load("hero/R4.png"), pygame.image.load("hero/R5.png"), pygame.image.load("hero/R6.png"),
              pygame.image.load("hero/R7.png"), pygame.image.load("hero/R8.png"), pygame.image.load("hero/R9.png")]
move_left = [pygame.image.load("hero/L1.png"), pygame.image.load("hero/L2.png"), pygame.image.load("hero/L3.png"),
             pygame.image.load("hero/L4.png"), pygame.image.load("hero/L5.png"), pygame.image.load("hero/L6.png"),
             pygame.image.load("hero/L7.png"), pygame.image.load("hero/L8.png"), pygame.image.load("hero/L9.png")]





move_rightE = [pygame.image.load("enemy2/Run__000.png"), pygame.image.load("enemy2/Run__001.png"),
               pygame.image.load("enemy2/Run__002.png"), pygame.image.load("enemy2/Run__003.png"),
               pygame.image.load("enemy2/Run__004.png"), pygame.image.load("enemy2/Run__005.png"),
               pygame.image.load("enemy2/Run__006.png"), pygame.image.load("enemy2/Run__006.png"),
               pygame.image.load("enemy2/Run__007.png"), pygame.image.load("enemy2/Run__008.png"),
               pygame.image.load("enemy2/Run__009.png")]
move_leftE = [pygame.image.load("enemy2/Run__000r.png"), pygame.image.load("enemy2/Run__001r.png"),
              pygame.image.load("enemy2/Run__002r.png"), pygame.image.load("enemy2/Run__003r.png"),
              pygame.image.load("enemy2/Run__004r.png"), pygame.image.load("enemy2/Run__005r.png"),
              pygame.image.load("enemy2/Run__006r.png"), pygame.image.load("enemy2/Run__006r.png"),
              pygame.image.load("enemy2/Run__007r.png"), pygame.image.load("enemy2/Run__008r.png"),
              pygame.image.load("enemy2/Run__009r.png")]













# these codes are for importing images



hero = pygame.image.load("hero/standing.png")

bulletSound = pygame.mixer.Sound("sounds/bullet.wav")
hitSound = pygame.mixer.Sound("sounds/hit.wav")
# create display window
SCREEN_HEIGHT = 640
SCREEN_WIDTH = 1280

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


backgroundImage = pygame.image.load("bg4.jpg")
screen.blit(backgroundImage, (0, 0))
myfont = pygame.font.SysFont('bold', 100)
my_font = pygame.font.SysFont('bold', 70)
main_menu = myfont.render('Main Menu  ', False, (225,225 , 225))
screen.blit(main_menu, (450, 20))
game_name = my_font.render('FATAL SHOT  ', False, (225,0, 0))
screen.blit(game_name, (480, 200))


# load button images
start_img = pygame.image.load('start_btn (2).png')
exit_img = pygame.image.load('exit_btn (2).png').convert_alpha()
credits_img = pygame.image.load('credits_btn.png').convert_alpha()
back_img = pygame.image.load('back_btn.png').convert_alpha()
replay_img = pygame.image.load('reply_btn.png').convert_alpha()

# create button instances

clock = pygame.time.Clock()
pygame.display.set_caption("The Fatal Shot")  # label of window
# RGB Color

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TEAL = (152, 251, 152)
OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 100, 0)
level = 1



# x = 10   # Movement in Horizontal (Default Position)
# y = 484   # Movement in vertical   (Default Position)
# width = 64 #because size of hero = 64
# height = 64
# Used in Player() Class
# left = False # Status of direction
# right = False
# moves = 0
# step = 6  # step is the magnitude of the Displacement and speed of hero movement
# speed = 10 # using for jumping (distance of jumping)
# isJumping = False #status of Jumping
font = pygame.font.SysFont("segoeui", 60, True)  # the font that show the score om screen
#names of team :
myfont = pygame.font.SysFont('Comic Sans MS', 50)
textsurface = myfont.render('Made by:  ', False, WHITE)
textsurface1 = myfont.render('Youssef Ashraf ', False, WHITE)
textsurface2 = myfont.render('Mahmoud Khaled  ', False, WHITE)
textsurface3 = myfont.render('Omar Mostafa  ', False, WHITE)
textsurface4 = myfont.render('Kariem Alaa  ', False, WHITE)
textsurface5 = myfont.render('Ahmed Abdelaziem ', False, WHITE)
textsurface6 = myfont.render('Ahmed Mohamed ', False, WHITE)