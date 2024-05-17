
"""
Created on Sun Aug  6 12:13:49 2023

@author: AlecPeters
"""

import random
import pygame
import pygame_gui
import sys
import general
import pandas as pd

def random_key():
    music_df = pd.read_csv(r'C:\Users\AlecPeters\guitar-practice\data\scales.csv')
    index_list = []
    for i in range(24):
        index_list.append(i)
    random_index = random.choice(index_list)
    return music_df['KEY'][random_index]

def in_key(key,note,pentatonic=False):
    music_df = pd.read_csv(r'C:\Users\AlecPeters\guitar-practice\data\scales.csv')
    key_df = music_df[music_df['KEY'] == key]
    key_list = key_df.values.tolist()

    for i in range(len(key_list[0])):
        if pentatonic:
            if key_list[0][8] == 'MAJOR' and (i != 4 and i !=7):
                if key_list[0][i] == note:
                    return True
            elif key_list[0][8] == 'MINOR' and (i != 2 and i !=6):
                if key_list[0][i] == note:
                    return True
        else:
            if key_list[0][i] == note:
                return True
    return False

def random_note(
        neck_choice = 'vertical',
        fret_start = 0,
        fret_end = 12,
        min_string = 1,
        max_string = 6,
        key = None,
        pentatonic = False
    ):

    # Read in data for full guitar neck
    df = pd.read_csv(r'C:\Users\AlecPeters\guitar-practice\data\guitar_neck.csv')

    # Filter down based on user input
    guitar_neck_df = df[(df['FRET'] >= fret_start) & (df['FRET'] <= fret_end) & (df['STRING'] >= min_string) & (df['STRING'] <= max_string)]
    guitar_neck = guitar_neck_df.values.tolist()

    # generate random index
    index_list = []
    for i in range(len(guitar_neck)):
        index_list.append(i)
    
    if key == None:
        random_index = random.choice(index_list)
        random_note = guitar_neck[random_index]
    else:
        flag = True
        while flag:
            random_index = random.choice(index_list)
            random_note = guitar_neck[random_index]
            note = random_note[3]
            if len(note) > 1:
                note_list = note.split('/')
                for i in note_list:
                    if in_key(key,i):
                        flag = False
                        random_note[3] = i
            else:
                if in_key(key,note):
                    flag = False

    return random_note

def counter(count = 0):
    new_count = count + 1
    return new_count
   
def main():
    
    # initalize game
    pygame.init()

    # screen size
    screen_width = 810
    screen_height = 645

    # set fonts
    font = pygame.font.SysFont('freesansbold.ttf', 32)
    small_font = pygame.font.SysFont("bahnschrift", 15)

    # set colors
    white = (255,255,255)
    black = (0,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    light_blue = (202, 228, 241)
    red = (255,0,0)

    # create screen 
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Name the Note | Alec Peters")

    # set images
    vertical_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\vertical_button_unclicked.png').convert_alpha()
    vertical_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\vertical_button_clicked.png').convert_alpha()
    horizontal_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\horizontal_button_unclicked.png').convert_alpha()
    horizontal_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\horizontal_button_clicked.png').convert_alpha()
    zero_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\zero_button_unclicked.png').convert_alpha()
    zero_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\zero_button_clicked.png').convert_alpha()
    one_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\one_button_unclicked.png').convert_alpha()
    one_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\one_button_clicked.png').convert_alpha()
    two_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\two_button_unclicked.png').convert_alpha()
    two_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\two_button_clicked.png').convert_alpha()
    three_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\three_button_unclicked.png').convert_alpha()
    three_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\three_button_clicked.png').convert_alpha()
    four_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\four_button_unclicked.png').convert_alpha()
    four_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\four_button_clicked.png').convert_alpha()
    five_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\five_button_unclicked.png').convert_alpha()
    five_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\five_button_clicked.png').convert_alpha()
    six_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\six_button_unclicked.png').convert_alpha()
    six_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\six_button_clicked.png').convert_alpha()
    seven_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\seven_button_unclicked.png').convert_alpha()
    seven_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\seven_button_clicked.png').convert_alpha()
    eight_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\eight_button_unclicked.png').convert_alpha()
    eight_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\eight_button_clicked.png').convert_alpha()
    nine_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\nine_button_unclicked.png').convert_alpha()
    nine_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\nine_button_clicked.png').convert_alpha()
    ten_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\ten_button_unclicked.png').convert_alpha()
    ten_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\ten_button_clicked.png').convert_alpha()
    eleven_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\eleven_button_unclicked.png').convert_alpha()
    eleven_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\eleven_button_clicked.png').convert_alpha()
    twelve_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\twelve_button_unclicked.png').convert_alpha()
    twelve_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\twelve_button_clicked.png').convert_alpha()
    a_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\a_key_button_unclicked.png').convert_alpha()
    a_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\a_key_button_clicked.png').convert_alpha()
    bb_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\bb_key_button_unclicked.png').convert_alpha()
    bb_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\bb_key_button_clicked.png').convert_alpha()
    b_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\b_key_button_unclicked.png').convert_alpha()
    b_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\b_key_button_clicked.png').convert_alpha()
    c_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\c_key_button_unclicked.png').convert_alpha()
    c_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\c_key_button_clicked.png').convert_alpha()
    db_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\db_key_button_unclicked.png').convert_alpha()
    db_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\db_key_button_clicked.png').convert_alpha()
    d_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\d_key_button_unclicked.png').convert_alpha()
    d_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\d_key_button_clicked.png').convert_alpha()
    eb_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\eb_key_button_unclicked.png').convert_alpha()
    eb_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\eb_key_button_clicked.png').convert_alpha()
    e_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\e_key_button_unclicked.png').convert_alpha()
    e_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\e_key_button_clicked.png').convert_alpha()
    f_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\f_key_button_unclicked.png').convert_alpha()
    f_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\f_key_button_clicked.png').convert_alpha()
    fsharp_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\fsharp_key_button_unclicked.png').convert_alpha()
    fsharp_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\fsharp_key_button_clicked.png').convert_alpha()
    g_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\g_key_button_unclicked.png').convert_alpha()
    g_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\g_key_button_clicked.png').convert_alpha()
    ab_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\ab_key_button_unclicked.png').convert_alpha()
    ab_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\ab_key_button_clicked.png').convert_alpha()
    am_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\am_key_button_unclicked.png').convert_alpha()
    am_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\am_key_button_clicked.png').convert_alpha()
    bbm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\bbm_key_button_unclicked.png').convert_alpha()
    bbm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\bbm_key_button_clicked.png').convert_alpha()
    bm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\bm_key_button_unclicked.png').convert_alpha()
    bm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\bm_key_button_clicked.png').convert_alpha()
    cm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\cm_key_button_unclicked.png').convert_alpha()
    cm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\cm_key_button_clicked.png').convert_alpha()
    csharpm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\csharpm_key_button_unclicked.png').convert_alpha()
    csharpm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\csharpm_key_button_clicked.png').convert_alpha()
    dm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\dm_key_button_unclicked.png').convert_alpha()
    dm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\dm_key_button_clicked.png').convert_alpha()
    dsharpm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\dsharpm_key_button_unclicked.png').convert_alpha()
    dsharpm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\dsharpm_key_button_clicked.png').convert_alpha()
    em_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\em_key_button_unclicked.png').convert_alpha()
    em_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\em_key_button_clicked.png').convert_alpha()
    fm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\fm_key_button_unclicked.png').convert_alpha()
    fm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\fm_key_button_clicked.png').convert_alpha()
    fsharpm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\fsharpm_key_button_unclicked.png').convert_alpha()
    fsharpm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\fsharpm_key_button_clicked.png').convert_alpha()
    gm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\gm_key_button_unclicked.png').convert_alpha()
    gm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\gm_key_button_clicked.png').convert_alpha()
    gsharpm_key_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\gsharpm_key_button_unclicked.png').convert_alpha()
    gsharpm_key_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\gsharpm_key_button_clicked.png').convert_alpha()
    e_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\e_button_unclicked.png').convert_alpha()
    e_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\e_button_clicked.png').convert_alpha()
    a_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\a_button_unclicked.png').convert_alpha()
    a_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\a_button_clicked.png').convert_alpha()
    d_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\d_button_unclicked.png').convert_alpha()
    d_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\d_button_clicked.png').convert_alpha()
    g_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\g_button_unclicked.png').convert_alpha()
    g_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\g_button_clicked.png').convert_alpha()
    b_button_unclicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\b_button_unclicked.png').convert_alpha()
    b_button_clicked_img = pygame.image.load(r'C:\Users\AlecPeters\music_quizzes\images\b_button_clicked.png').convert_alpha()

    # create buttons
    start_fret_y = 140
    end_fret_y = 240
    major_key_y = 340
    minor_key_y = 440
    string_y = 540

    vertical_button_unclicked = general.Button(200,35, vertical_button_unclicked_img,1)
    vertical_button_clicked = general.Button(200,35, vertical_button_clicked_img,1)
    vertical_button = vertical_button_unclicked
    horizontal_button_unclicked = general.Button(400,35, horizontal_button_unclicked_img,1)
    horizontal_button_clicked = general.Button(400,35, horizontal_button_clicked_img,1)
    horizontal_button = horizontal_button_unclicked
    zero_button_unclicked_a = general.Button(15,start_fret_y, zero_button_unclicked_img,1)
    zero_button_clicked_a = general.Button(15,start_fret_y, zero_button_clicked_img,1)
    zero_button_a = zero_button_unclicked_a
    zero_button_unclicked_b = general.Button(15,end_fret_y, zero_button_unclicked_img,1)
    zero_button_clicked_b = general.Button(15,end_fret_y, zero_button_clicked_img,1)
    zero_button_b = zero_button_unclicked_b
    one_button_unclicked_a = general.Button(75,start_fret_y, one_button_unclicked_img,1)
    one_button_clicked_a = general.Button(75,start_fret_y, one_button_clicked_img,1)
    one_button_a = one_button_unclicked_a
    one_button_unclicked_b = general.Button(75,end_fret_y, one_button_unclicked_img,1)
    one_button_clicked_b = general.Button(75,end_fret_y, one_button_clicked_img,1)
    one_button_b = one_button_unclicked_b
    two_button_unclicked_a = general.Button(135,start_fret_y, two_button_unclicked_img,1)
    two_button_clicked_a = general.Button(135,start_fret_y, two_button_clicked_img,1)
    two_button_a = two_button_unclicked_a
    two_button_unclicked_b = general.Button(135,end_fret_y, two_button_unclicked_img,1)
    two_button_clicked_b = general.Button(135,end_fret_y, two_button_clicked_img,1)
    two_button_b = two_button_unclicked_b
    three_button_unclicked_a = general.Button(195,start_fret_y, three_button_unclicked_img,1)
    three_button_clicked_a = general.Button(195,start_fret_y, three_button_clicked_img,1)
    three_button_a = three_button_unclicked_a
    three_button_unclicked_b = general.Button(195,end_fret_y, three_button_unclicked_img,1)
    three_button_clicked_b = general.Button(195,end_fret_y, three_button_clicked_img,1)
    three_button_b = three_button_unclicked_b
    four_button_unclicked_a = general.Button(255,start_fret_y, four_button_unclicked_img,1)
    four_button_clicked_a = general.Button(255,start_fret_y, four_button_clicked_img,1)
    four_button_a = four_button_unclicked_a
    four_button_unclicked_b = general.Button(255,end_fret_y, four_button_unclicked_img,1)
    four_button_clicked_b = general.Button(255,end_fret_y, four_button_clicked_img,1)
    four_button_b = four_button_unclicked_b
    five_button_unclicked_a = general.Button(315,start_fret_y, five_button_unclicked_img,1)
    five_button_clicked_a = general.Button(315,start_fret_y, five_button_clicked_img,1)
    five_button_a = five_button_unclicked_a
    five_button_unclicked_b = general.Button(315,end_fret_y, five_button_unclicked_img,1)
    five_button_clicked_b = general.Button(315,end_fret_y, five_button_clicked_img,1)
    five_button_b = five_button_unclicked_b
    six_button_unclicked_a = general.Button(375,start_fret_y, six_button_unclicked_img,1)
    six_button_clicked_a = general.Button(375,start_fret_y, six_button_clicked_img,1)
    six_button_a = six_button_unclicked_a
    six_button_unclicked_b = general.Button(375,end_fret_y, six_button_unclicked_img,1)
    six_button_clicked_b = general.Button(375,end_fret_y, six_button_clicked_img,1)
    six_button_b = six_button_unclicked_b
    seven_button_unclicked_a = general.Button(435,start_fret_y, seven_button_unclicked_img,1)
    seven_button_clicked_a = general.Button(435,start_fret_y, seven_button_clicked_img,1)
    seven_button_a = seven_button_unclicked_a
    seven_button_unclicked_b = general.Button(435,end_fret_y, seven_button_unclicked_img,1)
    seven_button_clicked_b = general.Button(435,end_fret_y, seven_button_clicked_img,1)
    seven_button_b = seven_button_unclicked_b
    eight_button_unclicked_a = general.Button(495,start_fret_y, eight_button_unclicked_img,1)
    eight_button_clicked_a = general.Button(495,start_fret_y, eight_button_clicked_img,1)
    eight_button_a = eight_button_unclicked_a
    eight_button_unclicked_b = general.Button(495,end_fret_y, eight_button_unclicked_img,1)
    eight_button_clicked_b = general.Button(495,end_fret_y, eight_button_clicked_img,1)
    eight_button_b = eight_button_unclicked_b
    nine_button_unclicked_a = general.Button(555,start_fret_y, nine_button_unclicked_img,1)
    nine_button_clicked_a = general.Button(555,start_fret_y, nine_button_clicked_img,1)
    nine_button_a = nine_button_unclicked_a
    nine_button_unclicked_b = general.Button(555,end_fret_y, nine_button_unclicked_img,1)
    nine_button_clicked_b = general.Button(555,end_fret_y, nine_button_clicked_img,1)
    nine_button_b = nine_button_unclicked_b
    ten_button_unclicked_a = general.Button(615,start_fret_y, ten_button_unclicked_img,1)
    ten_button_clicked_a = general.Button(615,start_fret_y, ten_button_clicked_img,1)
    ten_button_a = ten_button_unclicked_a
    ten_button_unclicked_b = general.Button(615,end_fret_y, ten_button_unclicked_img,1)
    ten_button_clicked_b = general.Button(615,end_fret_y, ten_button_clicked_img,1)
    ten_button_b = ten_button_unclicked_b
    eleven_button_unclicked_a = general.Button(675,start_fret_y, eleven_button_unclicked_img,1)
    eleven_button_clicked_a = general.Button(675,start_fret_y, eleven_button_clicked_img,1)
    eleven_button_a = eleven_button_unclicked_a
    eleven_button_unclicked_b = general.Button(675,end_fret_y, eleven_button_unclicked_img,1)
    eleven_button_clicked_b = general.Button(675,end_fret_y, eleven_button_clicked_img,1)
    eleven_button_b = eleven_button_unclicked_b
    twelve_button_unclicked_a = general.Button(735,start_fret_y, twelve_button_unclicked_img,1)
    twelve_button_clicked_a = general.Button(735,start_fret_y, twelve_button_clicked_img,1)
    twelve_button_a = twelve_button_unclicked_a
    twelve_button_unclicked_b = general.Button(735,end_fret_y, twelve_button_unclicked_img,1)
    twelve_button_clicked_b = general.Button(735,end_fret_y, twelve_button_clicked_img,1)
    twelve_button_b = twelve_button_unclicked_b
    a_key_button_unclicked = general.Button(50,major_key_y, a_key_button_unclicked_img,1)
    a_key_button_clicked = general.Button(50,major_key_y, a_key_button_clicked_img,1)
    a_key_button = a_key_button_unclicked
    bb_key_button_unclicked = general.Button(110,major_key_y, bb_key_button_unclicked_img,1)
    bb_key_button_clicked = general.Button(110,major_key_y, bb_key_button_clicked_img,1)
    bb_key_button = bb_key_button_unclicked
    b_key_button_unclicked = general.Button(170,major_key_y, b_key_button_unclicked_img,1)
    b_key_button_clicked = general.Button(170,major_key_y, b_key_button_clicked_img,1)
    b_key_button = b_key_button_unclicked
    c_key_button_unclicked = general.Button(230,major_key_y, c_key_button_unclicked_img,1)
    c_key_button_clicked = general.Button(230,major_key_y, c_key_button_clicked_img,1)
    c_key_button = c_key_button_unclicked
    db_key_button_unclicked = general.Button(290,major_key_y, db_key_button_unclicked_img,1)
    db_key_button_clicked = general.Button(290,major_key_y, db_key_button_clicked_img,1)
    db_key_button = db_key_button_unclicked
    d_key_button_unclicked = general.Button(350,major_key_y, d_key_button_unclicked_img,1)
    d_key_button_clicked = general.Button(350,major_key_y, d_key_button_clicked_img,1)
    d_key_button = d_key_button_unclicked
    eb_key_button_unclicked = general.Button(410,major_key_y, eb_key_button_unclicked_img,1)
    eb_key_button_clicked = general.Button(410,major_key_y, eb_key_button_clicked_img,1)
    eb_key_button = eb_key_button_unclicked
    e_key_button_unclicked = general.Button(470,major_key_y, e_key_button_unclicked_img,1)
    e_key_button_clicked = general.Button(470,major_key_y, e_key_button_clicked_img,1)
    e_key_button = e_key_button_unclicked
    f_key_button_unclicked = general.Button(530,major_key_y, f_key_button_unclicked_img,1)
    f_key_button_clicked = general.Button(530,major_key_y, f_key_button_clicked_img,1)
    f_key_button = f_key_button_unclicked
    fsharp_key_button_unclicked = general.Button(590,major_key_y, fsharp_key_button_unclicked_img,1)
    fsharp_key_button_clicked = general.Button(590,major_key_y, fsharp_key_button_clicked_img,1)
    fsharp_key_button = fsharp_key_button_unclicked
    g_key_button_unclicked = general.Button(650,major_key_y, g_key_button_unclicked_img,1)
    g_key_button_clicked = general.Button(650,major_key_y, g_key_button_clicked_img,1)
    g_key_button = g_key_button_unclicked
    ab_key_button_unclicked = general.Button(710,major_key_y, ab_key_button_unclicked_img,1)
    ab_key_button_clicked = general.Button(710,major_key_y, ab_key_button_clicked_img,1)
    ab_key_button = ab_key_button_unclicked
    am_key_button_unclicked = general.Button(50,minor_key_y, am_key_button_unclicked_img,1)
    am_key_button_clicked = general.Button(50,minor_key_y, am_key_button_clicked_img,1)
    am_key_button = am_key_button_unclicked
    bbm_key_button_unclicked = general.Button(110,minor_key_y, bbm_key_button_unclicked_img,1)
    bbm_key_button_clicked = general.Button(110,minor_key_y, bbm_key_button_clicked_img,1)
    bbm_key_button = bbm_key_button_unclicked
    bm_key_button_unclicked = general.Button(170,minor_key_y, bm_key_button_unclicked_img,1)
    bm_key_button_clicked = general.Button(170,minor_key_y, bm_key_button_clicked_img,1)
    bm_key_button = bm_key_button_unclicked
    cm_key_button_unclicked = general.Button(230,minor_key_y, cm_key_button_unclicked_img,1)
    cm_key_button_clicked = general.Button(230,minor_key_y, cm_key_button_clicked_img,1)
    cm_key_button = cm_key_button_unclicked
    csharpm_key_button_unclicked = general.Button(290,minor_key_y, csharpm_key_button_unclicked_img,1)
    csharpm_key_button_clicked = general.Button(290,minor_key_y, csharpm_key_button_clicked_img,1)
    csharpm_key_button = csharpm_key_button_unclicked
    dm_key_button_unclicked = general.Button(350,minor_key_y, dm_key_button_unclicked_img,1)
    dm_key_button_clicked = general.Button(350,minor_key_y, dm_key_button_clicked_img,1)
    dm_key_button = dm_key_button_unclicked
    dsharpm_key_button_unclicked = general.Button(410,minor_key_y, dsharpm_key_button_unclicked_img,1)
    dsharpm_key_button_clicked = general.Button(410,minor_key_y, dsharpm_key_button_clicked_img,1)
    dsharpm_key_button = dsharpm_key_button_unclicked
    em_key_button_unclicked = general.Button(470,minor_key_y, em_key_button_unclicked_img,1)
    em_key_button_clicked = general.Button(470,minor_key_y, em_key_button_clicked_img,1)
    em_key_button = em_key_button_unclicked
    fm_key_button_unclicked = general.Button(530,minor_key_y, fm_key_button_unclicked_img,1)
    fm_key_button_clicked = general.Button(530,minor_key_y, fm_key_button_clicked_img,1)
    fm_key_button = fm_key_button_unclicked
    fsharpm_key_button_unclicked = general.Button(590,minor_key_y, fsharpm_key_button_unclicked_img,1)
    fsharpm_key_button_clicked = general.Button(590,minor_key_y, fsharpm_key_button_clicked_img,1)
    fsharpm_key_button = fsharpm_key_button_unclicked
    gm_key_button_unclicked = general.Button(650,minor_key_y, gm_key_button_unclicked_img,1)
    gm_key_button_clicked = general.Button(650,minor_key_y, gm_key_button_clicked_img,1)
    gm_key_button = gm_key_button_unclicked
    gsharpm_key_button_unclicked = general.Button(710,minor_key_y, gsharpm_key_button_unclicked_img,1)
    gsharpm_key_button_clicked = general.Button(710,minor_key_y, gsharpm_key_button_clicked_img,1)
    gsharpm_key_button = gsharpm_key_button_unclicked
    elow_button_unclicked = general.Button(75,string_y, e_button_unclicked_img,1)
    elow_button_clicked = general.Button(75,string_y, e_button_clicked_img,1)
    elow_button = elow_button_unclicked
    a_button_unclicked = general.Button(185,string_y, a_button_unclicked_img,1)
    a_button_clicked = general.Button(185,string_y, a_button_clicked_img,1)
    a_button = a_button_unclicked
    d_button_unclicked = general.Button(295,string_y, d_button_unclicked_img,1)
    d_button_clicked = general.Button(295,string_y, d_button_clicked_img,1)
    d_button = d_button_unclicked
    g_button_unclicked = general.Button(405,string_y, g_button_unclicked_img,1)
    g_button_clicked = general.Button(405,string_y, g_button_clicked_img,1)
    g_button = g_button_unclicked
    b_button_unclicked = general.Button(515,string_y, b_button_unclicked_img,1)
    b_button_clicked = general.Button(515,string_y, b_button_clicked_img,1)
    b_button = b_button_unclicked
    ehigh_button_unclicked = general.Button(625,string_y, e_button_unclicked_img,1)
    ehigh_button_clicked = general.Button(625,string_y, e_button_clicked_img,1)
    ehigh_button = ehigh_button_unclicked
    
    clock = pygame.time.Clock()

    text = font.render('Enter Note: ', True, black, light_blue)
    note_question = text.get_rect()

    def recurring(user_input, count=None, right=None):
        
        neck_choice = user_input[0]
        fret_start = user_input[1]
        fret_end = user_input[2]
        string_start = user_input[3]
        string_end = user_input[4]
        key = user_input[5]

        question = random_note(neck_choice, fret_start, fret_end, string_start, string_end, key)

        # split sharps and flats into a list so wither can be right
        if len(question[3]) == 5:
            lower_answer = question[3].lower()
            correct_answer = lower_answer.split('/')
        else: 
            correct_answer = [question[3].lower()]

        # set count of questions asked
        if count == None:
            n = counter()
        else:
            n = counter(count)

        # set count of right answers
        if right == None:
            nright = 0
        else:
            nright = right

        # set/re-set guitar neck image
        if neck_choice == 'horizontal':
            guitar_neck_image = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\horizontal_guitar_neck_nb.png')
            neck_position = (90,320)
            note_question.center = (385,250)
            answer_position = (448, 235)
            new_text_1_loc = (405,250)
            new_text_2_loc = (410,350)
            new_text_3_loc = (483,330)
            continue_message_loc = (410,600)
            dot_loc = (question[6],question[7])
        else:
            guitar_neck_image = pygame.image.load(r'C:\Users\AlecPeters\guitar-practice\images\vertical_guitar_neck_nb.png')
            neck_position = (175,0)
            note_question.center = (470,250)
            answer_position = (535, 235)
            new_text_1_loc = (520,250)
            new_text_2_loc = (520,450)
            new_text_3_loc = (615,430)
            continue_message_loc = (530,600)
            dot_loc = (question[4],question[5])

        def show_answer(answer):

            while True:

                screen.fill(light_blue)
                screen.blit(guitar_neck_image,dest=neck_position)
                pygame.draw.circle(guitar_neck_image,red,dot_loc,5)
                #screen.blit(guitar_neck_image, (175,0))

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

                if answer.lower() in correct_answer:
                    questions_right = counter(nright)
                    message = "Score: " + str(round((questions_right/n)*100,2)) + "%"
                    new_text_1 = pygame.font.SysFont("bahnschrift", 50).render("Correct!", True, green)
                    new_text_1_rect = new_text_1.get_rect(center=(new_text_1_loc))
                    new_text_2 = pygame.font.SysFont("bahnschrift", 20).render(message, True, black)
                    new_text_2_rect = new_text_2.get_rect(center=(new_text_2_loc))
                    screen.blit(new_text_1, new_text_1_rect)
                    screen.blit(new_text_2, new_text_2_rect)
                else:
                    questions_right = nright
                    message = "Score: " + str(round((questions_right/n)*100,2)) + "%"
                    new_text_1 = pygame.font.SysFont("bahnschrift", 50).render("Incorrect", True, red)
                    new_text_1_rect = new_text_1.get_rect(center=(new_text_1_loc))
                    new_text_2 = pygame.font.SysFont("bahnschrift", 20).render(message, True, black)
                    new_text_2_rect = new_text_2.get_rect(center=(new_text_2_loc))
                    new_text_3 = pygame.font.SysFont("bahnschrift", 20).render(question[3], True, black)
                    new_text_3_rect = new_text_1.get_rect(center=(new_text_3_loc))
                    screen.blit(new_text_1, new_text_1_rect)
                    screen.blit(new_text_2, new_text_2_rect)
                    screen.blit(new_text_3, new_text_3_rect)

                continue_message = pygame.font.SysFont("bahnschrift", 15).render("Hit ENTER to continue. Hit SPACE to return to main", True, black)
                continue_message_rect = continue_message.get_rect(center=(continue_message_loc))
                screen.blit(continue_message, continue_message_rect)

                clock.tick(60)

                pygame.display.flip()

        def get_answer():
           
            manager = pygame_gui.UIManager((screen_width,screen_height))
            pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(answer_position, (30, 30)), manager=manager, object_id='#main_text_entry')

            question_number = small_font.render(str(n) , True, black, light_blue)
            question_numb_rect = question_number.get_rect()
            question_numb_rect.center = (50,50)
                                                    
            while True:
                
                UI_REFRESH_RATE = clock.tick(60)/1000
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                        event.ui_object_id == '#main_text_entry'):
                        show_answer(event.text)

                    manager.process_events(event)
                
                screen.fill(light_blue)
                screen.blit(text, note_question)
                screen.blit(question_number, question_numb_rect)
                screen.blit(guitar_neck_image, neck_position)
                pygame.draw.circle(guitar_neck_image,red,dot_loc,5)

                manager.update(UI_REFRESH_RATE)
                manager.draw_ui(screen)

                pygame.display.flip()

        get_answer()

    # screen one questions
    guitar_neck_view_question = pygame.font.SysFont("bahnschrift", 15).render('CHOOSE A GUITAR NECK', True, black, light_blue)
    guitar_neck_view_rect = text.get_rect()
    guitar_neck_view_rect.center = (370,25)
    starting_fret_question = pygame.font.SysFont("bahnschrift", 15).render('CHOOSE A STARTING FRET', True, black, light_blue)
    starting_fret_question_rect = text.get_rect()
    starting_fret_question_rect.center = (370,130)
    ending_fret_question = pygame.font.SysFont("bahnschrift", 15).render('CHOOSE AN ENDING FRET', True, black, light_blue)
    ending_fret_question_rect = text.get_rect()
    ending_fret_question_rect.center = (370,230)
    key_question = pygame.font.SysFont("bahnschrift", 15).render('CHOOSE A KEY', True, black, light_blue)
    key_question_rect = text.get_rect()
    key_question_rect.center = (410,330)
    strings_question = pygame.font.SysFont("bahnschrift", 15).render('CHOOSE STRINGS', True, black, light_blue)
    strings_question_rect = text.get_rect()
    strings_question_rect.center = (410,530)

    string_input_list = []

    while True:

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
                elif event.key == pygame.K_RETURN:
                    input_list = [neck_view, start_fret, end_fret, min(string_input_list), max(string_input_list), input_key]
                    recurring(input_list)

        # fill in screen backgroun
        screen.fill(light_blue)

        # input questions
        screen.blit(guitar_neck_view_question, guitar_neck_view_rect)
        screen.blit(starting_fret_question, starting_fret_question_rect)
        screen.blit(ending_fret_question, ending_fret_question_rect)
        screen.blit(key_question, key_question_rect)
        screen.blit(strings_question, strings_question_rect)

        # guitr neck view buttons
        if vertical_button_unclicked.draw(screen):
            vertical_button = vertical_button_clicked
            neck_view = 'vertical'
        else:
            vertical_button.draw(screen)
        if horizontal_button_unclicked.draw(screen):
            horizontal_button = horizontal_button_clicked
            neck_view = 'horizontal'
        else:
            horizontal_button.draw(screen)
        
        # starting fret buttons
        if zero_button_unclicked_a.draw(screen):
            zero_button_a = zero_button_clicked_a
            start_fret = 0
        else:
            zero_button_a.draw(screen)
        if one_button_unclicked_a.draw(screen):
            one_button_a = one_button_clicked_a
            start_fret = 1
        else:
            one_button_a.draw(screen)
        if two_button_unclicked_a.draw(screen):
            two_button_a = two_button_clicked_a
            start_fret = 2
        else:
            two_button_a.draw(screen)
        if three_button_unclicked_a.draw(screen):
            three_button_a = three_button_clicked_a
            start_fret = 3
        else:
            three_button_a.draw(screen)
        if four_button_unclicked_a.draw(screen):
            four_button_a = four_button_clicked_a
            start_fret = 4
        else:
            four_button_a.draw(screen)
        if five_button_unclicked_a.draw(screen):
            five_button_a = five_button_clicked_a
            start_fret = 5
        else:
            five_button_a.draw(screen)
        if six_button_unclicked_a.draw(screen):
            six_button_a = six_button_clicked_a
            start_fret = 6
        else:
            six_button_a.draw(screen)
        if seven_button_unclicked_a.draw(screen):
            seven_button_a = seven_button_clicked_a
            start_fret = 7
        else:
            seven_button_a.draw(screen)
        if eight_button_unclicked_a.draw(screen):
            eight_button_a = eight_button_clicked_a
            start_fret = 8
        else:
            eight_button_a.draw(screen)
        if nine_button_unclicked_a.draw(screen):
            nine_button_a = nine_button_clicked_a
            start_fret = 9
        else:
            nine_button_a.draw(screen)
        if ten_button_unclicked_a.draw(screen):
            ten_button_a = ten_button_clicked_a
            start_fret = 10
        else:
            ten_button_a.draw(screen)
        if eleven_button_unclicked_a.draw(screen):
            eleven_button_a = eleven_button_clicked_a
            start_fret = 11
        else:
            eleven_button_a.draw(screen)
        if twelve_button_unclicked_a.draw(screen):
            twelve_button_a = twelve_button_clicked_a
            start_fret = 12
        else:
            twelve_button_a.draw(screen)

        # ending fret buttons
        if zero_button_unclicked_b.draw(screen):
            zero_button_b = zero_button_clicked_b
            end_fret = 0
        else:
            zero_button_b.draw(screen)
        if one_button_unclicked_b.draw(screen):
            one_button_b = one_button_clicked_b
            end_fret = 1
        else:
            one_button_b.draw(screen)
        if two_button_unclicked_b.draw(screen):
            two_button_b = two_button_clicked_b
            end_fret = 2
        else:
            two_button_b.draw(screen)
        if three_button_unclicked_b.draw(screen):
            three_button_b = three_button_clicked_b
            end_fret = 3
        else:
            three_button_b.draw(screen)
        if four_button_unclicked_b.draw(screen):
            four_button_b = four_button_clicked_b
            end_fret = 4
        else:
            four_button_b.draw(screen)
        if five_button_unclicked_b.draw(screen):
            five_button_b = five_button_clicked_b
            end_fret = 5
        else:
            five_button_b.draw(screen)
        if six_button_unclicked_b.draw(screen):
            six_button_b = six_button_clicked_b
            end_fret = 6
        else:
            six_button_b.draw(screen)
        if seven_button_unclicked_b.draw(screen):
            seven_button_b = seven_button_clicked_b
            end_fret = 7
        else:
            seven_button_b.draw(screen)
        if eight_button_unclicked_b.draw(screen):
            eight_button_b = eight_button_clicked_b
            end_fret = 8
        else:
            eight_button_b.draw(screen)
        if nine_button_unclicked_b.draw(screen):
            nine_button_b = nine_button_clicked_b
            end_fret = 9
        else:
            nine_button_b.draw(screen)
        if ten_button_unclicked_b.draw(screen):
            ten_button_b = ten_button_clicked_b
            end_fret = 10
        else:
            ten_button_b.draw(screen)
        if eleven_button_unclicked_b.draw(screen):
            eleven_button_b = eleven_button_clicked_b
            end_fret = 11
        else:
            eleven_button_b.draw(screen)
        if twelve_button_unclicked_b.draw(screen):
            twelve_button_b = twelve_button_clicked_b
            end_fret = 12
        else:
            twelve_button_b.draw(screen)

        # major key buttons
        if a_key_button_unclicked.draw(screen):
            a_key_button = a_key_button_clicked
            input_key = 'A MAJOR'
        else:
            a_key_button.draw(screen)  
        if bb_key_button_unclicked.draw(screen):
            bb_key_button = bb_key_button_clicked
            input_key = 'Bb MAJOR'
        else:
            bb_key_button.draw(screen)
        if b_key_button_unclicked.draw(screen):
            b_key_button = b_key_button_clicked
            input_key = 'B MAJOR'
        else:
            b_key_button.draw(screen) 
        if c_key_button_unclicked.draw(screen):
            c_key_button = c_key_button_clicked
            input_key = 'C MAJOR'
        else:
            c_key_button.draw(screen)   
        if db_key_button_unclicked.draw(screen):
            db_key_button = db_key_button_clicked
            input_key = 'Db MAJOR'
        else:
            db_key_button.draw(screen)
        if d_key_button_unclicked.draw(screen):
            d_key_button = d_key_button_clicked
            input_key = 'D MAJOR'
        else:
            d_key_button.draw(screen)
        if eb_key_button_unclicked.draw(screen):
            eb_key_button = eb_key_button_clicked
            input_key = 'Eb MAJOR'
        else:
            eb_key_button.draw(screen)
        if e_key_button_unclicked.draw(screen):
            e_key_button = e_key_button_clicked
            input_key = 'E MAJOR'
        else:
            e_key_button.draw(screen)
        if f_key_button_unclicked.draw(screen):
            f_key_button = f_key_button_clicked
            input_key = 'F MAJOR'
        else:
            f_key_button.draw(screen)
        if fsharp_key_button_unclicked.draw(screen):
            fsharp_key_button = fsharp_key_button_clicked
            input_key = 'F MAJOR'
        else:
            fsharp_key_button.draw(screen)
        if g_key_button_unclicked.draw(screen):
            g_key_button = g_key_button_clicked
            input_key = 'G MAJOR'
        else:
            g_key_button.draw(screen)
        if ab_key_button_unclicked.draw(screen):
            ab_key_button = ab_key_button_clicked
            input_key = 'Ab MAJOR'
        else:
            ab_key_button.draw(screen)

        # minor key buttons
        if am_key_button_unclicked.draw(screen):
            am_key_button = am_key_button_clicked
            input_key = 'A MINOR'
        else:
            am_key_button.draw(screen)
        if bbm_key_button_unclicked.draw(screen):
            bbm_key_button = bbm_key_button_clicked
            input_key = 'Bb MINOR'
        else:
            bbm_key_button.draw(screen)
        if bm_key_button_unclicked.draw(screen):
            bm_key_button = bm_key_button_clicked
            input_key = 'B MINOR'
        else:
            bm_key_button.draw(screen)
        if cm_key_button_unclicked.draw(screen):
            cm_key_button = cm_key_button_clicked
            input_key = 'C MINOR'
        else:
            cm_key_button.draw(screen)
        if csharpm_key_button_unclicked.draw(screen):
            csharpm_key_button = csharpm_key_button_clicked
            input_key = 'C# MINOR'
        else:
            csharpm_key_button.draw(screen)
        if dm_key_button_unclicked.draw(screen):
            dm_key_button = dm_key_button_clicked
            input_key = 'D MINOR'
        else:
            dm_key_button.draw(screen)
        if dsharpm_key_button_unclicked.draw(screen):
            dsharpm_key_button = dsharpm_key_button_clicked
            input_key = 'D# MINOR'
        else:
            dsharpm_key_button.draw(screen)
        if em_key_button_unclicked.draw(screen):
            em_key_button = em_key_button_clicked
            input_key = 'E MINOR'
        else:
            em_key_button.draw(screen)
        if fm_key_button_unclicked.draw(screen):
            fm_key_button = fm_key_button_clicked
            input_key = 'F MINOR'
        else:
            fm_key_button.draw(screen)
        if fsharpm_key_button_unclicked.draw(screen):
            fsharpm_key_button = fsharpm_key_button_clicked
            input_key = 'F# MINOR'
        else:
            fsharpm_key_button.draw(screen)
        if gm_key_button_unclicked.draw(screen):
            gm_key_button = gm_key_button_clicked
            input_key = 'G MINOR'
        else:
            gm_key_button.draw(screen)
        if gsharpm_key_button_unclicked.draw(screen):
            gsharpm_key_button = gsharpm_key_button_clicked
            input_key = 'G# MINOR'
        else:
            gsharpm_key_button.draw(screen)

        # strings buttons
        if elow_button_unclicked.draw(screen):
            elow_button = elow_button_clicked
            string_input_list.append(1)
        else:
            elow_button.draw(screen)
        if a_button_unclicked.draw(screen):
            a_button = a_button_clicked
            string_input_list.append(2)
        else:
            a_button.draw(screen)
        if d_button_unclicked.draw(screen):
            d_button = d_button_clicked
            string_input_list.append(3)
        else:
            d_button.draw(screen)
        if g_button_unclicked.draw(screen):
            g_button = g_button_clicked
            string_input_list.append(4)
        else:
            g_button.draw(screen)
        if b_button_unclicked.draw(screen):
            b_button = b_button_clicked
            string_input_list.append(5)
        else:
            b_button.draw(screen)
        if ehigh_button_unclicked.draw(screen):
            ehigh_button = ehigh_button_clicked
            string_input_list.append(6)
        else:
            ehigh_button.draw(screen)

        instruct_message = small_font.render("Hit SPACE to clear selections. Hit ENTER to continue", True, black, light_blue)
        instruct_message_rect = instruct_message.get_rect(center=((screen_width/2,620)))
        screen.blit(instruct_message, instruct_message_rect)

        pygame.display.update()

#main()
#print(in_key('A MINOR','F',True))
#random_key()
print(random_note(key='F# MINOR'))