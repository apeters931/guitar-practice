import pandas as pd
import random

def read_data(tab_name):

    data = pd.read_excel("data/music_spreadsheet.xlsx", sheet_name=tab_name)
    return data

quiz_type = input(
    """
    Select what you would like to be quized on.

    A. Chords 
    B. Diatonic Scales 
    C. Pentatonic Scales
    D. Modes

    """
    )

if quiz_type == "A":
    df = read_data("Chords")
    flag = True
    difficulty = input(
        """
        Select difficulty.

        1. Easy
        2. Medium
        3. Hard

        """
    )
    counter = 0
    while flag:
        n = random.randint(0,len(df.index)-1)
        if int(difficulty) == df.loc[n]['Multiplier']:
            counter = counter + 1
            chord = df.loc[n]['Chords']
            answer = input(str(counter) + ". What notes are in " + chord + ": ")
            if answer == df.loc[n]['Notes']:
                print("Yes!")
            else:
                print("No:(")
                print(df.loc[n]['Notes'])
            keep_playing = input("Do you want to continue (Y/N)? ")
            if keep_playing == 'N':
                flag = False

elif quiz_type == "B":
    df = read_data("Diatonic Scales")
    flag = True
    counter = 1
    while flag:
        n = random.randint(0,len(df.index)-1)
        key = df.loc[n]['NOTE'] + df.loc[n]['MAJOR/MINOR']
        answer = input(str(counter) + ". What notes are in " + key + ": ")
        if answer == df.loc[n]['SCALE']:
            print("Yes!")
        else:
            print("No:(")
            print(df.loc[n]['SCALE'])
        keep_playing = input("Do you want to continue (Y/N)? ")
        if keep_playing == 'N':
            flag = False
        counter = counter + 1

elif quiz_type == "C":
    df = read_data("Pentatonic Scales")
    flag = True
    counter = 1
    while flag:
        n = random.randint(0,len(df.index)-1)
        key = df.loc[n]['NOTE'] + df.loc[n]['MAJOR/MINOR']
        answer = input( str(counter) + ". What notes are in " + key + ": ")
        if answer == df.loc[n]['SCALE']:
            print("Yes!")
        else:
            print("No:(")
            print(df.loc[n]['SCALE'])
        keep_playing = input("Do you want to continue (Y/N)? ")
        if keep_playing == 'N':
            flag = False
        counter = counter + 1

elif quiz_type == "D":
    df = read_data("Modes")
    flag = True
    counter = 1
    while flag:
        n = random.randint(0,len(df.index)-1)
        key = df.loc[n]['ROOT'] + ' ' + df.loc[n]['MODE']
        answer = input( str(counter) + ". What notes are in " + key + ": ")
        if answer == df.loc[n]['NOTES']:
            print("Yes!")
        else:
            print("No:(")
            print(df.loc[n]['NOTES'])
        keep_playing = input("Do you want to continue (Y/N)? ")
        if keep_playing == 'N':
            flag = False
        counter = counter + 1

else: 
    print("Please choose valid response")
