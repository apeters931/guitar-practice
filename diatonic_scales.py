### TO DO ###
# continue comments
# add game logic that exists in the CL game
# fix spacing in game

### IMPORT PACKAGES ###
# package needed for pygame functionality
import pygame
# used for exiting the python desktop app when you click exit
import sys
# used for reading in excel sheet
import pandas as pd
# for reusing functions that can me shared with the other music quizzs
import music_quizzes_main as m

### PYGAME FORMATTING VARIABLES ###
def main(type):
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
  question_x = 390
  question_y = 200
  answer_x = 300
  answer_x_increment = 14
  old_answer_x = 400
  answer_y = 300
  old_answer_y = 300
  correct_message_x = 400
  correct_message_y = 350
  incorrect_message_x1 = 400
  incorrect_message_y1 = 350
  incorrect_message_x2 = 410
  incorrect_message_y2 = 425
  # fonts
  font = pygame.font.SysFont('freesans', 32)
  # create screen 
  screen = pygame.display.set_mode((screen_width,screen_height))
  pygame.display.set_caption("Diatonic Scales | Alec Peters")

  def get_answer():
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
    if type == 'diatonic_scale':
      key_and_answer = m.diatonic_scale()
      question_text = "What notes are in " + key_and_answer[0] + '?'
    elif type == 'pentatonic_scale':
      key_and_answer = m.pentatonic_scale()
      question_text = "What pentatonic notes are in " + key_and_answer[0] + '?'

    question = font.render(question_text, True, black, light_blue)
    question_rect = question.get_rect()
    question_rect.center = (question_x,question_y)

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
            x = answer_x + (answer_x_increment*counter)
            globals()[f"text_rect{counter + 1}"].center = (x,answer_y)
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
            # print(input_list) # use for troubleshooting
            # print(answer)
            show_answer(key_and_answer,answer)
        
      if key_pressed:
        counter = counter + 1
        screen.fill(light_blue)
        screen.blit(question,question_rect)
        for i in range(1,counter+1):
          screen.blit(globals()[f"text{i}"], globals()[f"text_rect{i}"])
        
      elif key_pressed == False:
        if counter == 0:
          screen.fill(light_blue)
          screen.blit(question,question_rect)
          pygame.display.update()
        else:
          screen.fill(light_blue)
          for i in range(1,counter+1):
            screen.blit(question,question_rect)
            screen.blit(globals()[f"text{i}"], globals()[f"text_rect{i}"])
          pygame.display.update()

  def show_answer(answer,input):

    answer_list = []
    input_list = []
    input_str = ''

    answer_str = answer[1].lower()
    answer_list = answer_str.split(',')
    for i in input:
      input_list.append(i.lower())
    for i in input:
      input_str = input_str + i + ' '

    print(answer_list)
    print(input_list)

    if answer_list == input_list:
      message_text = "Correct!"
      message = font.render(message_text, True, green, light_blue)
      message_rect = message.get_rect()
      message_rect.center = (correct_message_x,correct_message_y)
    
    else:
      message_text = "Incorrect"
      message_text_2 = answer[1]
      message = font.render(message_text, True, red, light_blue)
      message_2 = font.render(message_text_2, True, red, light_blue)
      message_rect = message.get_rect()
      message_2_rect = message_2.get_rect()
      message_rect.center = (incorrect_message_x1,incorrect_message_y1)
      message_2_rect.center = (incorrect_message_x2,incorrect_message_y2)

    question_text = "What notes are in " + answer[0] + '?'
    question = font.render(question_text, True, black, light_blue)
    question_rect = question.get_rect()
    question_rect.center = (question_x,question_y)

    old_answer = font.render(input_str, True, black, light_blue)
    old_answer_rect = old_answer.get_rect()
    old_answer_rect.center = (old_answer_x,old_answer_y)

  ### PYGAME LOOP ###
    while True:

      screen.fill(light_blue)
      screen.blit(question,question_rect)
      screen.blit(old_answer,old_answer_rect)
      screen.blit(message,message_rect)

      if answer_list != input_list:
        screen.blit(message_2,message_2_rect)

      for event in pygame.event.get():

        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            get_answer()

      pygame.display.update()

  get_answer()  

main('pentatonic_scale')
#main('diatonic_scale')