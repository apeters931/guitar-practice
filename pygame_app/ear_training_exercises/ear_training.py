import pandas as pd
import random
import os


def pick_notes(notes):
    df = pd.read_csv(r'C:\Users\AlecPeters\guitar-practice\data\ear_training.csv')
    ear_training_df = df[df['root_name'].isin(notes)]
    ear_training = ear_training_df.values.tolist()

    index_list = []
    for i in range(len(ear_training)):
        index_list.append(i)

    random_index = random.choice(index_list)
    question_note = ear_training[random_index]

    return question_note

def get_mp3_file(note,root=None):
    if len(note) == 6:
        note = note.replace('/','-')
    if root:
        if len(root) == 6:
            root = note.replace('/','-')
    base_path = r'C:\Users\AlecPeters\guitar-practice\mp3'
    file_extension = r'.mp3'
    if root != None:
        file_name = root + '_' + note + file_extension
    else:
        file_name = note + file_extension
    file_path = os.path.join(base_path,file_name)

    return file_path

def random_note():

    note_list = ['A','A#/Bb','B','C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab']
    index_list = []

    for i in range(len(note_list)):
        index_list.append(i)

    random_index = random.choice(index_list)
    note = note_list[random_index]

    return note