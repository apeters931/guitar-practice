### TO DO ###
# fix tabs
# continue comments
# add game logic that exists in the CL game
# fix spacing in game


### IMPORT PACKAGES ###
# package needed for pygame functionality
import pygame
# used for exiting the python desktop app when you click exit
import sys

### PYGAME FORMATTING VARIABLES ###
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
# fonts
font = pygame.font.SysFont('freesans', 32)
# create screen 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Diatonic Scales | Alec Peters")

### INITIALIZE VARIABLES ###
# counter used for 
counter = 0
# used for special logic that is needed for consecutive backspaces 
backspace_counter = 0
# used for idividual letters or '#' input by users
input = ''
# used to add input (but combines sharps and flats with the notes); includes spaces
input_list = []
# list used for final answer without spaces
answer = []

### PYGAME LOOP ###
while True:
  
  key_pressed = False
  
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      if event.key != pygame.K_RSHIFT and event.key != pygame.K_LSHIFT and event.key != pygame.K_BACKSPACE and event.key != pygame.K_RETURN:     
        key = str(event.unicode)
        backspace_counter = 0
        if (key.isalpha or key == '#') and event.key != pygame.K_SPACE:
          input = input + key
        if event.key == pygame.K_SPACE:
          #print(input) # use for troubleshooting
          input_list.append(input)
          answer.append(input)
          input = ''
          input_list.append(' ')
        key_pressed = True
        globals()[f"text{counter + 1}"] = font.render(key, True, black, light_blue)
        globals()[f"text_rect{counter + 1}"] = globals()[f"text{counter + 1}"].get_rect()
        x = 200 + (15*counter)
        globals()[f"text_rect{counter + 1}"].center = (x,200)
      elif event.key == pygame.K_BACKSPACE and counter != 0:
        backspace_counter = backspace_counter + 1
        if backspace_counter == 1:
            input_list.append(input)
            if input_list[-1] != ' ':
                answer.append(input)
        counter = counter - 1
        if input_list[-1] != ' ':
            answer.pop(-1)
        input_list.pop(-1)
        input = ''
      elif event.key == pygame.K_RETURN:
          print(input)
          if input != '':
            input_list.append(input)
            answer.append(input)
          backpace_counter = 0
          #print(input_list) # use for troubleshooting
          print(answer)

    elif event.type == pygame.KEYUP:       
      if event.key == pygame.K_a:
        key_pressed = False
     
  if key_pressed:
    counter = counter + 1
    screen.fill(light_blue)
    for i in range(1,counter+1):
      screen.blit(globals()[f"text{i}"], globals()[f"text_rect{i}"])
    
  elif key_pressed == False:
    if counter == 0:
        screen.fill(light_blue)
        pygame.display.update()
    else:
        screen.fill(light_blue)
        for i in range(1,counter+1):
          screen.blit(globals()[f"text{i}"], globals()[f"text_rect{i}"])
        pygame.display.update()
