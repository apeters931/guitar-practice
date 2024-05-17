import pygame
import pygame_gui
import general
import sys
import ear_training

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
    pygame.display.set_caption("Identify the Note | Alec Peters")

    # set images
    a_key_button_unclicked_img = pygame.image.load(r'images\a_key_button_unclicked.png').convert_alpha()
    a_key_button_clicked_img = pygame.image.load(r'images\a_key_button_clicked.png').convert_alpha()
    bb_key_button_unclicked_img = pygame.image.load(r'images\bb_key_button_unclicked.png').convert_alpha()
    bb_key_button_clicked_img = pygame.image.load(r'images\bb_key_button_clicked.png').convert_alpha()
    b_key_button_unclicked_img = pygame.image.load(r'images\b_key_button_unclicked.png').convert_alpha()
    b_key_button_clicked_img = pygame.image.load(r'images\b_key_button_clicked.png').convert_alpha()
    c_key_button_unclicked_img = pygame.image.load(r'images\c_key_button_unclicked.png').convert_alpha()
    c_key_button_clicked_img = pygame.image.load(r'images\c_key_button_clicked.png').convert_alpha()
    db_key_button_unclicked_img = pygame.image.load(r'images\db_key_button_unclicked.png').convert_alpha()
    db_key_button_clicked_img = pygame.image.load(r'images\db_key_button_clicked.png').convert_alpha()
    d_key_button_unclicked_img = pygame.image.load(r'images\d_key_button_unclicked.png').convert_alpha()
    d_key_button_clicked_img = pygame.image.load(r'images\d_key_button_clicked.png').convert_alpha()
    eb_key_button_unclicked_img = pygame.image.load(r'images\eb_key_button_unclicked.png').convert_alpha()
    eb_key_button_clicked_img = pygame.image.load(r'images\eb_key_button_clicked.png').convert_alpha()
    e_key_button_unclicked_img = pygame.image.load(r'images\e_key_button_unclicked.png').convert_alpha()
    e_key_button_clicked_img = pygame.image.load(r'images\e_key_button_clicked.png').convert_alpha()
    f_key_button_unclicked_img = pygame.image.load(r'images\f_key_button_unclicked.png').convert_alpha()
    f_key_button_clicked_img = pygame.image.load(r'images\f_key_button_clicked.png').convert_alpha()
    fsharp_key_button_unclicked_img = pygame.image.load(r'images\fsharp_key_button_unclicked.png').convert_alpha()
    fsharp_key_button_clicked_img = pygame.image.load(r'images\fsharp_key_button_clicked.png').convert_alpha()
    g_key_button_unclicked_img = pygame.image.load(r'images\g_key_button_unclicked.png').convert_alpha()
    g_key_button_clicked_img = pygame.image.load(r'images\g_key_button_clicked.png').convert_alpha()
    ab_key_button_unclicked_img = pygame.image.load(r'images\ab_key_button_unclicked.png').convert_alpha()
    ab_key_button_clicked_img = pygame.image.load(r'images\ab_key_button_clicked.png').convert_alpha()
    play_button_image = pygame.image.load(r'images\play_button.png')

    # create buttons
    top_y = 200
    bottom_y = 300
    a_key_button_unclicked = general.Button(235,top_y, a_key_button_unclicked_img,1)
    a_key_button_clicked = general.Button(235,top_y, a_key_button_clicked_img,1)
    a_key_button = a_key_button_unclicked
    bb_key_button_unclicked = general.Button(295,top_y, bb_key_button_unclicked_img,1)
    bb_key_button_clicked = general.Button(295,top_y, bb_key_button_clicked_img,1)
    bb_key_button = bb_key_button_unclicked
    b_key_button_unclicked = general.Button(355,top_y, b_key_button_unclicked_img,1)
    b_key_button_clicked = general.Button(355,top_y, b_key_button_clicked_img,1)
    b_key_button = b_key_button_unclicked
    c_key_button_unclicked = general.Button(415,top_y, c_key_button_unclicked_img,1)
    c_key_button_clicked = general.Button(415,top_y, c_key_button_clicked_img,1)
    c_key_button = c_key_button_unclicked
    db_key_button_unclicked = general.Button(475,top_y, db_key_button_unclicked_img,1)
    db_key_button_clicked = general.Button(475,top_y, db_key_button_clicked_img,1)
    db_key_button = db_key_button_unclicked
    d_key_button_unclicked = general.Button(535,top_y, d_key_button_unclicked_img,1)
    d_key_button_clicked = general.Button(535,top_y, d_key_button_clicked_img,1)
    d_key_button = d_key_button_unclicked
    eb_key_button_unclicked = general.Button(235,bottom_y, eb_key_button_unclicked_img,1)
    eb_key_button_clicked = general.Button(235,bottom_y, eb_key_button_clicked_img,1)
    eb_key_button = eb_key_button_unclicked
    e_key_button_unclicked = general.Button(295,bottom_y, e_key_button_unclicked_img,1)
    e_key_button_clicked = general.Button(295,bottom_y, e_key_button_clicked_img,1)
    e_key_button = e_key_button_unclicked
    f_key_button_unclicked = general.Button(355,bottom_y, f_key_button_unclicked_img,1)
    f_key_button_clicked = general.Button(355,bottom_y, f_key_button_clicked_img,1)
    f_key_button = f_key_button_unclicked
    fsharp_key_button_unclicked = general.Button(415,bottom_y, fsharp_key_button_unclicked_img,1)
    fsharp_key_button_clicked = general.Button(415,bottom_y, fsharp_key_button_clicked_img,1)
    fsharp_key_button = fsharp_key_button_unclicked
    g_key_button_unclicked = general.Button(475,bottom_y, g_key_button_unclicked_img,1)
    g_key_button_clicked = general.Button(475,bottom_y, g_key_button_clicked_img,1)
    g_key_button = g_key_button_unclicked
    ab_key_button_unclicked = general.Button(535,bottom_y, ab_key_button_unclicked_img,1)
    ab_key_button_clicked = general.Button(535,bottom_y, ab_key_button_clicked_img,1)
    ab_key_button = ab_key_button_unclicked
    play_button = general.Button(300,250,play_button_image,1)

    # create text
    choose_note_question = small_font.render('CHOOSE NOTES TO BE QUIZED ON', True, black, light_blue)
    choose_note_question_rect = choose_note_question.get_rect(center=((screen_width/2,100)))
    final_question = small_font.render('What note is this?', True, black, light_blue)
    final_question_rect = final_question.get_rect(center=((390,225)))
    instruct_message = small_font.render("Hit SPACE to clear selections. Hit ENTER to continue", True, black, light_blue)
    instruct_message_rect = instruct_message.get_rect(center=((screen_width/2,620)))
    correct_message = small_font.render("Correct!", True, green)
    correct_message_rect = correct_message.get_rect(center=(screen_width/2,200))
    incorrect_message = small_font.render("Incorrect!", True, red)
    incorrect_message_rect = incorrect_message.get_rect(center=(screen_width/2,200))
    continue_message = small_font.render("Hit ENTER to continue. Hit SPACE to return to main", True, black)
    continue_message_rect = continue_message.get_rect(center=(screen_width/2,620))

    # timer
    clock = pygame.time.Clock()

    def recurring(user_input, count=None, right=None):

        # get random note from available notes
        question = ear_training.pick_notes(user_input)
        #play_note = 'placeholder'
        play_note = pygame.mixer.Sound(ear_training.get_mp3_file(question[1]))

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
            play_button.draw(screen)
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
                        if play_button.checkForInput(pygame.mouse.get_pos()):
                            #print(play_note)
                            play_note.play()
                
                if answer.lower() in correct_answer:
                    questions_right = general.counter(nright)
                    message = "Score: " + str(round((questions_right/n)*100,2)) + "%"
                    score_message = small_font.render(message, True, black)
                    score_message_rect = score_message.get_rect(center=(screen_width/2,250))
                    screen.blit(correct_message, correct_message_rect)
                    screen.blit(score_message, score_message_rect)
                else:
                    questions_right = nright
                    message = "Score: " + str(round((questions_right/n)*100,2)) + "%"
                    score_message = small_font.render(message, True, black)
                    score_message_rect = score_message.get_rect(center=(screen_width/2,225))
                    correct_answer_message = small_font.render(question[0], True, black)
                    correct_answer_message_rect = correct_answer_message.get_rect(center=(screen_width/2,250))
                    screen.blit(incorrect_message, incorrect_message_rect)
                    screen.blit(score_message, score_message_rect)
                    screen.blit(correct_answer_message, correct_answer_message_rect)
                
                pygame.display.flip()

        def get_answer(): 

            # get user input
            manager = pygame_gui.UIManager((screen_width,screen_height))
            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((460,207), (30, 30)), manager=manager, object_id='#main_text_entry')

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
                        if play_button.checkForInput(pygame.mouse.get_pos()):
                            #print(play_note)
                            play_note.play()
                    elif (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                        event.ui_object_id == '#main_text_entry'):
                        show_answer(event.text)

                    manager.process_events(event)
                
                screen.fill(light_blue)
                screen.blit(final_question, final_question_rect)
                screen.blit(question_number, question_numb_rect)
                play_button.draw(screen)
                manager.update(UI_REFRESH_RATE)
                manager.draw_ui(screen)
                pygame.display.flip()

        get_answer()

    # game logic
    note_input_list = []
    while True:

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                elif event.key == pygame.K_RETURN:
                    input_list = note_input_list
                    recurring(input_list)
                    
        # fill in screen backgroun
        screen.fill(light_blue)

        # input questions / instructions
        screen.blit(choose_note_question, choose_note_question_rect)
        screen.blit(instruct_message, instruct_message_rect )

        # button clicking logic
        if a_key_button_unclicked.draw(screen):
            a_key_button = a_key_button_clicked
            note_input_list.append('a')
        else:
            a_key_button.draw(screen)  
        if bb_key_button_unclicked.draw(screen):
            bb_key_button = bb_key_button_clicked
            note_input_list.append('a#/bb')
        else:
            bb_key_button.draw(screen)
        if b_key_button_unclicked.draw(screen):
            b_key_button = b_key_button_clicked
            note_input_list.append('b')
        else:
            b_key_button.draw(screen) 
        if c_key_button_unclicked.draw(screen):
            c_key_button = c_key_button_clicked
            note_input_list.append('c')
        else:
            c_key_button.draw(screen)   
        if db_key_button_unclicked.draw(screen):
            db_key_button = db_key_button_clicked
            note_input_list.append('c#/db')
        else:
            db_key_button.draw(screen)
        if d_key_button_unclicked.draw(screen):
            d_key_button = d_key_button_clicked
            note_input_list.append('d')
        else:
            d_key_button.draw(screen)
        if eb_key_button_unclicked.draw(screen):
            eb_key_button = eb_key_button_clicked
            note_input_list.append('d#/eb')
        else:
            eb_key_button.draw(screen)
        if e_key_button_unclicked.draw(screen):
            e_key_button = e_key_button_clicked
            note_input_list.append('e')
        else:
            e_key_button.draw(screen)
        if f_key_button_unclicked.draw(screen):
            f_key_button = f_key_button_clicked
            note_input_list.append('f')
        else:
            f_key_button.draw(screen)
        if fsharp_key_button_unclicked.draw(screen):
            fsharp_key_button = fsharp_key_button_clicked
            note_input_list.append('f#/gb')
        else:
            fsharp_key_button.draw(screen)
        if g_key_button_unclicked.draw(screen):
            g_key_button = g_key_button_clicked
            note_input_list.append('g')
        else:
            g_key_button.draw(screen)
        if ab_key_button_unclicked.draw(screen):
            ab_key_button = ab_key_button_clicked
            note_input_list.append('g#/ab')
        else:
            ab_key_button.draw(screen)

        pygame.display.update()


#main()
