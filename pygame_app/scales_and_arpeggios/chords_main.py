### IMPORT PACKAGES ###
# package needed for pygame functionality
import pygame
# used for exiting the python desktop app when you click exit
import sys
import game_logic
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
  text = "choose difficulty"
  # text cordinates
  text_x = screen_width/2
  text_y = 120
  # fonts
  font = pygame.font.SysFont('freesans', 32)
  # create screen 
  screen = pygame.display.set_mode((screen_width,screen_height))
  pygame.display.set_caption("Scales & Arpeggios | Alec Peters")
  # spacing
  easy_button_x = 330
  easy_button_y = 190
  medium_button_x = 310
  medium_button_y = 290
  difficult_button_x = 313
  difficult_button_y = 390

  # set images
  easy_unclicked_img = pygame.image.load(r'pygame_app\images\easy_button_unclicked.png').convert_alpha()
  easy_clicked_img = pygame.image.load(r'pygame_app\images\easy_button_clicked.png').convert_alpha()
  medium_unclicked_img = pygame.image.load(r'pygame_app\images\medium_button_unclicked.png').convert_alpha()
  medium_clicked_img = pygame.image.load(r'pygame_app\images\medium_button_clicked.png').convert_alpha()
  difficult_unclicked_img = pygame.image.load(r'pygame_app\images\difficult_button_unclicked.png').convert_alpha()
  difficult_clicked_img = pygame.image.load(r'pygame_app\images\difficult_button_clicked.png').convert_alpha()
  # set buttons
  easy_button_unclicked = general.Button(easy_button_x,easy_button_y,easy_unclicked_img,1)
  easy_button_clicked = general.Button(easy_button_x,easy_button_y,easy_clicked_img,1)
  easy_button = easy_button_unclicked
  medium_button_unclicked = general.Button(medium_button_x,medium_button_y,medium_unclicked_img,1)
  medium_button_clicked = general.Button(medium_button_x,medium_button_y,medium_clicked_img,1)
  medium_button = medium_button_unclicked
  difficult_button_unclicked = general.Button(difficult_button_x,difficult_button_y,difficult_unclicked_img,1)
  difficult_button_clicked = general.Button(difficult_button_x,difficult_button_y,difficult_clicked_img,1)
  difficult_button = difficult_button_unclicked

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

      if easy_button_unclicked.draw(screen):
        easy_button = easy_button_clicked
        game_logic.main('chords',1)
      else:
        easy_button.draw(screen)
      if medium_button_unclicked.draw(screen):
        medium_button = medium_button_clicked
        game_logic.main('chords',2)
      else:
        medium_button.draw(screen)
      if difficult_button_unclicked.draw(screen):
        difficult_button = difficult_button_clicked
        game_logic.main('chords',3)
      else:
        difficult_button.draw(screen)
    
      pygame.display.update()