import pandas as pd
import random

def read_data(tab_name):

    data = pd.read_excel("data/music_spreadsheet.xlsx", sheet_name=tab_name)
    return data

def main():
    quiz_type = input(
        "\nSelect what you would like to be quized on.\nA. Chords\nB. Diatonic Scales\nC. Pentatonic Scales\nD. Modes\n\n"
        )

    if quiz_type == "A":
        df = read_data("Chords")
        flag = True
        difficulty = input(
            "\nSelect difficulty.\n1. Easy\n2. Medium\n3. Hard\n\n"
        )
        counter = 0
        while flag:
            n = random.randint(0,len(df.index)-1)
            if int(difficulty) == df.loc[n]['Multiplier']:
                counter = counter + 1
                chord = df.loc[n]['Chords']
                answer = input("\n" + str(counter) + ". What notes are in " + chord + ": ")
                if answer == df.loc[n]['Notes']:
                    print("\nYes!")
                else:
                    print("\nNo:(")
                    print(df.loc[n]['Notes'])
                keep_playing = input("\nDo you want to continue (Y/N)? ")
                if keep_playing == 'N':
                    flag = False

    elif quiz_type == "B":
        df = read_data("Diatonic Scales")
        flag = True
        counter = 1
        while flag:
            n = random.randint(0,len(df.index)-1)
            key = df.loc[n]['NOTE'] + df.loc[n]['MAJOR/MINOR']
            answer = input("\n" + str(counter) + ". What notes are in " + key + ": ")
            if answer == df.loc[n]['SCALE']:
                print("\nYes!")
            else:
                print("\nNo:(")
                print(df.loc[n]['SCALE'])
            keep_playing = input("\nDo you want to continue (Y/N)? ")
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
            answer = input("\n" + str(counter) + ". What notes are in " + key + ": ")
            if answer == df.loc[n]['SCALE']:
                print("\nYes!")
            else:
                print("\nNo:(")
                print(df.loc[n]['SCALE'])
            keep_playing = input("\nDo you want to continue (Y/N)? ")
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
            answer = input("\n" + str(counter) + ". What notes are in " + key + ": ")
            if answer == df.loc[n]['NOTES']:
                print("\nYes!")
            else:
                print("\nNo:(")
                print(df.loc[n]['NOTES'])
            keep_playing = input("\nDo you want to continue (Y/N)? ")
            if keep_playing == 'N':
                flag = False
            counter = counter + 1

    else: 
        print("Please choose valid response")
