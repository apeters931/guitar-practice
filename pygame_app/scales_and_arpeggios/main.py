### IMPORT PACKAGES ###
# package needed for pygame functionality
import pygame
# used for exiting the python desktop app when you click exit
import sys

sys.path.insert(1,'C:\\Users\\AlecPeters\\guitar-practice\\pygame_app\\general_package')
import general

# initalize game
pygame.init()
# screen size
screen_width = 810
screen_height = 645
# colors
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
light_blue = (202, 228, 241)
red = (255,0,0)
# text cordinates
# fonts
font = pygame.font.SysFont('freesans', 32)
# create screen 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Scales & Arpeggios | Alec Peters")
# set images
diatonic_scales_unclicked_img = pygame.image.load(r'pygame_app\images\diatonic_scales_unclicked.png').convert_alpha()
diatonic_scales_clicked_img = pygame.image.load(r'pygame_app\images\diatonic_scales_clicked.png').convert_alpha()
# set buttons
diatonic_scales_button_unclicked = general.Button(120,250,diatonic_scales_unclicked_img,1)
diatonic_scales_button_clicked = general.Button(120,250,diatonic_scales_clicked_img,1)
diatonic_button = diatonic_scales_button_unclicked

while True:
  
  screen.fill(light_blue)
  
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

  if diatonic_scales_button_unclicked.draw(screen):
    diatonic_button = diatonic_scales_button_clicked
  else:
    diatonic_button.draw(screen)
  
  pygame.display.update()