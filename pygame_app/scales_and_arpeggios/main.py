### IMPORT PACKAGES ###
# package needed for pygame functionality
import pygame
# used for exiting the python desktop app when you click exit
import sys
import game_logic
import chords_main
sys.path.insert(1,'C:\\Users\\AlecPeters\\guitar-practice\\pygame_app\\general_package')
import general

def main():
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
  # text
  text = "choose what you want to be quizzed on"
  # text cordinates
  text_x = screen_width/2
  text_y = 120
  # fonts
  font = pygame.font.SysFont('freesans', 32)
  # create screen 
  screen = pygame.display.set_mode((screen_width,screen_height))
  pygame.display.set_caption("Scales & Arpeggios | Alec Peters")
  # spacing
  diatonic_button_x = 260
  diatonic_button_y = 190
  pentatonic_button_x = 245
  pentatonic_button_y = 290
  chords_button_x = 313
  chords_button_y = 390
  modes_button_x = 316
  modes_button_y = 490

  # set images
  diatonic_scales_unclicked_img = pygame.image.load(r'pygame_app\images\diatonic_scales_button_unclicked.png').convert_alpha()
  diatonic_scales_clicked_img = pygame.image.load(r'pygame_app\images\diatonic_scales_button_clicked.png').convert_alpha()
  pentatonic_scales_unclicked_img = pygame.image.load(r'pygame_app\images\pentatonic_scales_button_unclicked.png').convert_alpha()
  pentatonic_scales_clicked_img = pygame.image.load(r'pygame_app\images\pentatonic_scales_button_clicked.png').convert_alpha()
  chords_unclicked_img = pygame.image.load(r'pygame_app\images\chords_button_unclicked.png').convert_alpha()
  chords_clicked_img = pygame.image.load(r'pygame_app\images\chords_button_clicked.png').convert_alpha()
  modes_unclicked_img = pygame.image.load(r'pygame_app\images\modes_button_unclicked.png').convert_alpha()
  modes_clicked_img = pygame.image.load(r'pygame_app\images\modes_button_clicked.png').convert_alpha()
  # set buttons
  diatonic_scales_button_unclicked = general.Button(diatonic_button_x,diatonic_button_y,diatonic_scales_unclicked_img,1)
  diatonic_scales_button_clicked = general.Button(diatonic_button_x,diatonic_button_y,diatonic_scales_clicked_img,1)
  diatonic_button = diatonic_scales_button_unclicked
  pentatonic_scales_button_unclicked = general.Button(pentatonic_button_x,pentatonic_button_y,pentatonic_scales_unclicked_img,1)
  pentatonic_scales_button_clicked = general.Button(pentatonic_button_x,pentatonic_button_y,pentatonic_scales_clicked_img,1)
  pentatonic_button = pentatonic_scales_button_unclicked
  modes_button_unclicked = general.Button(modes_button_x,modes_button_y,modes_unclicked_img,1)
  modes_button_clicked = general.Button(modes_button_x,modes_button_y,modes_clicked_img,1)
  modes_button = modes_button_unclicked
  chords_button_unclicked = general.Button(chords_button_x,chords_button_y,chords_unclicked_img,1)
  chords_button_clicked = general.Button(chords_button_x,chords_button_y,chords_clicked_img,1)
  chords_button = chords_button_unclicked

  title = font.render(text, True, black, light_blue)
  title_rect = title.get_rect()
  title_rect.center = (text_x,text_y)

  while True:
    
    screen.fill(light_blue)
    screen.blit(title,title_rect)
    
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

    if diatonic_scales_button_unclicked.draw(screen):
      diatonic_button = diatonic_scales_button_clicked
      game_logic.main('pentatonic_scale')
    else:
      diatonic_button.draw(screen)
    if pentatonic_scales_button_unclicked.draw(screen):
      pentatonic_button = pentatonic_scales_button_clicked
      game_logic.main('diatonic_scale')
    else:
      pentatonic_button.draw(screen)
    if chords_button_unclicked.draw(screen):
      chords_button = chords_button_clicked
      chords_main.main()
    else:
      chords_button.draw(screen)
    if modes_button_unclicked.draw(screen):
      modes_button = modes_button_clicked
      game_logic.main('modes')
    else:
      modes_button.draw(screen)
    
    pygame.display.update()