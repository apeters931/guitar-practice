import pygame
import pygame_gui
import general
import sys
import ear_training
import random

def random_interval(interval_list):

    index_list = []
    for i in range(len(interval_list)):
        index_list.append(i)
    
    random_index = random.choice(index_list)
    interval = interval_list[random_index]

    return interval

def main():

    # initalize game
    pygame.init()

    # screen size
    screen_width = 810
    screen_height = 645

    # set fonts
    small_font = pygame.font.SysFont("bahnschrift", 15)

    # set colors
    black = (0,0,0)
    green = (0,255,0)
    light_blue = (202, 228, 241)
    red = (255,0,0)

    # create screen 
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Find the Note | Alec Peters")

    # set images
    second_button_unclicked_img = pygame.image.load(r'images\2nd_button_unclicked.png').convert_alpha()
    second_button_clicked_img = pygame.image.load(r'images\2nd_button_clicked.png').convert_alpha()
    minor_third_button_unclicked_img = pygame.image.load(r'images\minor_3rd_button_unclicked.png').convert_alpha()
    minor_third_button_clicked_img = pygame.image.load(r'images\minor_3rd_button_clicked.png').convert_alpha()
    major_third_button_unclicked_img = pygame.image.load(r'images\major_3rd_button_unclicked.png').convert_alpha()
    major_third_button_clicked_img = pygame.image.load(r'images\major_3rd_button_clicked.png').convert_alpha()
    fourth_button_unclicked_img = pygame.image.load(r'images\4th_button_unclicked.png').convert_alpha()
    fourth_button_clicked_img = pygame.image.load(r'images\4th_button_clicked.png').convert_alpha()
    flat_fifth_button_unclicked_img = pygame.image.load(r'images\flat_5th_button_unclicked.png').convert_alpha()
    flat_fifth_button_clicked_img = pygame.image.load(r'images\flat_5th_button_clicked.png').convert_alpha()
    fifth_button_unclicked_img = pygame.image.load(r'images\5th_button_unclicked.png').convert_alpha()
    fifth_button_clicked_img = pygame.image.load(r'images\5th_button_clicked.png').convert_alpha()
    sharp_fifth_button_unclicked_img = pygame.image.load(r'images\sharp_5th_button_unclicked.png').convert_alpha()
    sharp_fifth_button_clicked_img = pygame.image.load(r'images\sharp_5th_button_clicked.png').convert_alpha()
    sixth_button_unclicked_img = pygame.image.load(r'images\6th_button_unclicked.png').convert_alpha()
    sixth_button_clicked_img = pygame.image.load(r'images\6th_button_clicked.png').convert_alpha()
    minor_seventh_button_unclicked_img = pygame.image.load(r'images\minor_7th_button_unclicked.png').convert_alpha()
    minor_seventh_button_clicked_img = pygame.image.load(r'images\minor_7th_button_clicked.png').convert_alpha()
    major_seventh_button_unclicked_img = pygame.image.load(r'images\major_7th_button_unclicked.png').convert_alpha()
    major_seventh_button_clicked_img = pygame.image.load(r'images\major_7th_button_clicked.png').convert_alpha()
    octive_button_unclicked_img = pygame.image.load(r'images\octive_button_unclicked.png').convert_alpha()
    octive_button_clicked_img = pygame.image.load(r'images\octive_button_clicked.png').convert_alpha()
    ninth_button_unclicked_img = pygame.image.load(r'images\9th_button_unclicked.png').convert_alpha()
    ninth_button_clicked_img = pygame.image.load(r'images\9th_button_clicked.png').convert_alpha()
    sharp_ninth_button_unclicked_img = pygame.image.load(r'images\sharp_9th_button_unclicked.png').convert_alpha()
    sharp_ninth_button_clicked_img = pygame.image.load(r'images\sharp_9th_button_clicked.png').convert_alpha()
    eleventh_button_unclicked_img = pygame.image.load(r'images\11th_button_unclicked.png').convert_alpha()
    eleventh_button_clicked_img = pygame.image.load(r'images\11th_button_clicked.png').convert_alpha()
    thirteenth_button_unclicked_img = pygame.image.load(r'images\13th_button_unclicked.png').convert_alpha()
    thirteenth_button_clicked_img = pygame.image.load(r'images\13th_button_clicked.png').convert_alpha()
    play_button_image = pygame.image.load(r'images\play_button.png')

    # create buttons
    top_y = 200
    middle_y = 300
    bottom_y = 400
    second_button_unclicked = general.Button(70,top_y, second_button_unclicked_img,1)
    second_button_clicked = general.Button(70,top_y, second_button_clicked_img,1)
    second_button = second_button_unclicked
    minor_third_button_unclicked = general.Button(200,top_y, minor_third_button_unclicked_img,1)
    minor_third_button_clicked = general.Button(200,top_y, minor_third_button_clicked_img,1)
    minor_third_button = minor_third_button_unclicked
    major_third_button_unclicked = general.Button(330,top_y, major_third_button_unclicked_img,1)
    major_third_button_clicked = general.Button(330,top_y, major_third_button_clicked_img,1)
    major_third_button = major_third_button_unclicked
    fourth_button_unclicked = general.Button(460,top_y, fourth_button_unclicked_img,1)
    fourth_button_clicked = general.Button(460,top_y, fourth_button_clicked_img,1)
    fourth_button = fourth_button_unclicked
    flat_fifth_button_unclicked = general.Button(590,top_y, flat_fifth_button_unclicked_img,1)
    flat_fifth_button_clicked = general.Button(590,top_y, flat_fifth_button_clicked_img,1)
    flat_fifth_button = flat_fifth_button_unclicked
    fifth_button_unclicked = general.Button(70,middle_y, fifth_button_unclicked_img,1)
    fifth_button_clicked = general.Button(70,middle_y, fifth_button_clicked_img,1)
    fifth_button = fifth_button_unclicked
    sharp_fifth_button_unclicked = general.Button(200,middle_y, sharp_fifth_button_unclicked_img,1)
    sharp_fifth_button_clicked = general.Button(200,middle_y, sharp_fifth_button_clicked_img,1)
    sharp_fifth_button = sharp_fifth_button_unclicked
    sixth_button_unclicked = general.Button(330,middle_y, sixth_button_unclicked_img,1)
    sixth_button_clicked = general.Button(330,middle_y, sixth_button_clicked_img,1)
    sixth_button = sixth_button_unclicked
    major_seventh_button_unclicked = general.Button(460,middle_y, major_seventh_button_unclicked_img,1)
    major_seventh_button_clicked = general.Button(460,middle_y, major_seventh_button_clicked_img,1)
    major_seventh_button = major_seventh_button_unclicked
    minor_seventh_button_unclicked = general.Button(590,middle_y, minor_seventh_button_unclicked_img,1)
    minor_seventh_button_clicked = general.Button(590,middle_y, minor_seventh_button_clicked_img,1)
    minor_seventh_button = minor_seventh_button_unclicked
    octive_button_unclicked = general.Button(70,bottom_y, octive_button_unclicked_img,1)
    octive_button_clicked = general.Button(70,bottom_y, octive_button_clicked_img,1)
    octive_button = octive_button_unclicked
    ninth_button_unclicked = general.Button(200,bottom_y, ninth_button_unclicked_img,1)
    ninth_button_clicked = general.Button(200,bottom_y, ninth_button_clicked_img,1)
    ninth_button = ninth_button_unclicked
    sharp_ninth_button_unclicked = general.Button(330,bottom_y, sharp_ninth_button_unclicked_img,1)
    sharp_ninth_button_clicked = general.Button(330,bottom_y, sharp_ninth_button_clicked_img,1)
    sharp_ninth_button = sharp_ninth_button_unclicked
    eleventh_button_unclicked = general.Button(460,bottom_y, eleventh_button_unclicked_img,1)
    eleventh_button_clicked = general.Button(460,bottom_y, eleventh_button_clicked_img,1)
    eleventh_button = eleventh_button_unclicked
    thirteenth_button_unclicked = general.Button(590,bottom_y, thirteenth_button_unclicked_img,1)
    thirteenth_button_clicked = general.Button(590,bottom_y, thirteenth_button_clicked_img,1)
    thirteenth_button = thirteenth_button_unclicked
    play_button_1 = general.Button(300,130,play_button_image,1)
    play_button_2 = general.Button(200,330,play_button_image,1)
    play_button_3 = general.Button(400,330,play_button_image,1)

    # create text
    choose_interval_question = small_font.render('CHOOSE INTERVALS TO BE QUIZED ON', True, black, light_blue)
    choose_interval_question_rect = choose_interval_question.get_rect(center=((screen_width/2,100)))
    final_question = small_font.render('What interval is this?', True, black, light_blue)
    final_question_rect = final_question.get_rect(center=(((screen_width/2)-15,80)))
    instruct_message = small_font.render("Hit SPACE to clear selections. Hit ENTER to continue", True, black, light_blue)
    instruct_message_rect = instruct_message.get_rect(center=((screen_width/2,620)))
    continue_message = small_font.render("Hit ENTER to continue. Hit SPACE to return to main", True, black)
    continue_message_rect = continue_message.get_rect(center=(screen_width/2,620))
    root_text = small_font.render("Root Note", True, black)
    root_text_rect = root_text.get_rect(center=(screen_width/2,150))
    interval_text = small_font.render("Interval Note", True, black)
    interval_text_rect = interval_text.get_rect(center=(300,350))
    both_text = small_font.render("Notes Played Together", True, black)
    both_text_rect = both_text.get_rect(center=(500,350))
    correct_message = small_font.render("Correct!", True, green)
    correct_message_rect = correct_message.get_rect(center=(screen_width/2,60))
    incorrect_message = small_font.render("Incorrect!", True, red)
    incorrect_message_rect = incorrect_message.get_rect(center=(screen_width/2,60))

    # timer
    clock = pygame.time.Clock()

    def recurring(user_input, count=None, right=None):

        # get random note from available notes
        interval_flag = True
        while interval_flag:
            note = ear_training.random_note()
            question = ear_training.pick_notes([note.lower()])
            interval = random_interval(interval_input_list)
            if question[interval[1]] != '0':
                interval_flag = False
        
        root_note = pygame.mixer.Sound(ear_training.get_mp3_file(question[1]))
        interval_note = pygame.mixer.Sound(ear_training.get_mp3_file(question[interval[1]]))

        # variables that need to be declared in recurring
        correct_answer_message = small_font.render(question[0], True, black)
        correct_answer_message_rect = correct_answer_message.get_rect(center=(460,80))

        # split sharps and flats 
        if len(question[0]) == 5:
            lower_answer = question[0].lower()
            correct_answer = lower_answer.split('/')
        else: 
            correct_answer = [question[0].lower()]
        
        # set count of questions asked
        if count == None:
            n = general.counter()
        else:
            n = general.counter(count)

        # set count of right answers
        if right == None:
            nright = 0
        else:
            nright = right

        def show_answer(answer):

            screen.fill(light_blue)
            play_button_1.draw(screen)
            play_button_2.draw(screen)
            play_button_3.draw(screen)
            screen.blit(root_text, root_text_rect)
            screen.blit(interval_text, interval_text_rect)
            screen.blit(both_text, both_text_rect)
            screen.blit(continue_message, continue_message_rect)

            while True:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            main()
                        elif event.key == pygame.K_RETURN:
                            games_played = n
                            recurring(input_list,games_played,questions_right)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if play_button_1.checkForInput(pygame.mouse.get_pos()):
                            root_note.play()
                        elif play_button_2.checkForInput(pygame.mouse.get_pos()):
                            interval_note.play()
                        elif play_button_3.checkForInput(pygame.mouse.get_pos()):
                            root_note.play()
                            interval_note.play()
                
                if answer.lower() == interval[0]:
                    questions_right = general.counter(nright)
                    message = "Score: " + str(round((questions_right/n)*100,2)) + "%"
                    score_message = small_font.render(message, True, black)
                    score_message_rect = score_message.get_rect(center=(screen_width/2,90))
                    correct_answer_message = small_font.render(interval[0] + ', ' + question[0] + ', ' + question[interval[1]].rstrip('1234'), True, black)
                    correct_answer_message_rect = correct_answer_message.get_rect(center=(screen_width/2,75))
                    screen.blit(correct_message, correct_message_rect)
                    screen.blit(score_message, score_message_rect)
                    screen.blit(correct_answer_message, correct_answer_message_rect)
                else:
                    questions_right = nright
                    message = "Score: " + str(round((questions_right/n)*100,2)) + "%"
                    score_message = small_font.render(message, True, black)
                    score_message_rect = score_message.get_rect(center=(screen_width/2,90))
                    correct_answer_message = small_font.render(interval[0] + ', ' + question[0] + ', ' + question[interval[1]].rstrip('1234'), True, black)
                    correct_answer_message_rect = correct_answer_message.get_rect(center=(screen_width/2,75))
                    screen.blit(incorrect_message, incorrect_message_rect)
                    screen.blit(score_message, score_message_rect)
                    screen.blit(correct_answer_message, correct_answer_message_rect)
                
                pygame.display.flip()

        def get_answer():

            # get user input
            manager = pygame_gui.UIManager((screen_width,screen_height))
            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((465,62), (30, 30)), manager=manager, object_id='#main_text_entry')

            question_number = small_font.render(str(n) , True, black, light_blue)
            question_numb_rect = question_number.get_rect()
            question_numb_rect.center = (50,50)

            while True:
                
                UI_REFRESH_RATE = clock.tick(60)/1000
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if play_button_1.checkForInput(pygame.mouse.get_pos()):
                            root_note.play()
                        elif play_button_2.checkForInput(pygame.mouse.get_pos()):
                            interval_note.play()
                        elif play_button_3.checkForInput(pygame.mouse.get_pos()):
                            root_note.play()
                            interval_note.play()
                    elif (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                        event.ui_object_id == '#main_text_entry'):
                        show_answer(event.text)

                    manager.process_events(event)
                
                screen.fill(light_blue)
                screen.blit(final_question, final_question_rect)
                screen.blit(question_number, question_numb_rect)
                screen.blit(root_text, root_text_rect)
                screen.blit(interval_text, interval_text_rect)
                screen.blit(both_text, both_text_rect)
                play_button_1.draw(screen)
                play_button_2.draw(screen)
                play_button_3.draw(screen)
                manager.update(UI_REFRESH_RATE)
                manager.draw_ui(screen)
                pygame.display.flip()

        get_answer()

    # game logic
    interval_input_list = []
    while True:

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                elif event.key == pygame.K_RETURN:
                    input_list = interval_input_list
                    recurring(input_list)
                    
        # fill in screen backgroun
        screen.fill(light_blue)

        # input questions / instructions
        screen.blit(choose_interval_question, choose_interval_question_rect)
        screen.blit(instruct_message, instruct_message_rect)

        # button clicking logic
        if second_button_unclicked.draw(screen):
            second_button = second_button_clicked
            second_list = ['2nd',8]
            interval_input_list.append(second_list)
        else:
            second_button.draw(screen)  
        if minor_third_button_unclicked.draw(screen):
            minor_third_button = minor_third_button_clicked
            minor_third_list = ['minor 3rd',9]
            interval_input_list.append(minor_third_list)
        else:
            minor_third_button.draw(screen)
        if major_third_button_unclicked.draw(screen):
            major_third_button = major_third_button_clicked
            major_third_list = ['major 3rd',10]
            interval_input_list.append(major_third_list)
        else:
            major_third_button.draw(screen) 
        if fourth_button_unclicked.draw(screen):
            fourth_button = fourth_button_clicked
            fourth_list = ['4th',11]
            interval_input_list.append(fourth_list)
        else:
            fourth_button.draw(screen)   
        if flat_fifth_button_unclicked.draw(screen):
            flat_fifth_button = flat_fifth_button_clicked
            flat_fifth_list = ['flat 5th',12]
            interval_input_list.append(flat_fifth_list)
        else:
            flat_fifth_button.draw(screen)
        if fifth_button_unclicked.draw(screen):
            fifth_button = fifth_button_clicked
            fifth_list = ['5th',13]
            interval_input_list.append(fifth_list)
        else:
            fifth_button.draw(screen)
        if sharp_fifth_button_unclicked.draw(screen):
           sharp_fifth_button = sharp_fifth_button_clicked
           sharp_fifth_list = ['sharp 5th',14]
           interval_input_list.append(sharp_fifth_list)
        else:
            sharp_fifth_button.draw(screen)
        if sixth_button_unclicked.draw(screen):
            sixth_button = sixth_button_clicked
            sixth_list = ['6th',15]
            interval_input_list.append(sixth_list)
        else:
            sixth_button.draw(screen)
        if minor_seventh_button_unclicked.draw(screen):
            minor_seventh_button = minor_seventh_button_clicked
            minor_seventh_list = ['minor 7th',16]
            interval_input_list.append(minor_seventh_list)
        else:
            minor_seventh_button.draw(screen)
        if major_seventh_button_unclicked.draw(screen):
            major_seventh_button = major_seventh_button_clicked
            major_seventh_list = ['major 7th',17]
            interval_input_list.append(major_seventh_list)
        else:
            major_seventh_button.draw(screen)
        if octive_button_unclicked.draw(screen):
            octive_button = octive_button_clicked
            octive_list = ['octive',18]
            interval_input_list.append(octive_list)
        else:
            octive_button.draw(screen)
        if ninth_button_unclicked.draw(screen):
            ninth_button = ninth_button_clicked
            ninth_list = ['9th',19]
            interval_input_list.append(ninth_list)
        else:
            ninth_button.draw(screen)
        if sharp_ninth_button_unclicked.draw(screen):
            sharp_ninth_button = sharp_ninth_button_clicked
            sharp_ninth_list = ['sharp ninth',20]
            interval_input_list.append(sharp_ninth_list)
        else:
            sharp_ninth_button.draw(screen)
        if eleventh_button_unclicked.draw(screen):
            eleventh_button = eleventh_button_clicked
            eleventh_list = ['11th',21]
            interval_input_list.append(eleventh_list)
        else:
            eleventh_button.draw(screen)
        if thirteenth_button_unclicked.draw(screen):
            thirteenth_button = thirteenth_button_clicked
            thirteenth_list = ['13th',22]
            interval_input_list.append(thirteenth_list)
        else:
            thirteenth_button.draw(screen)

        pygame.display.update()

#main()