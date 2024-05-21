# Guitar Practice :guitar:

Different ways to virtually practice guitar. The modules in this program will help you with naviating the fretboard, understanding/memorizing important elements of music theory, and training your ear to recognize pitch and intervals

# How to Use

1. clone repo to your home directory
2. open terminal and navigate to the cloned directory
3. run `py main.py`
4. input module you would like to play and any other variables

# Modules

## Guitar Fretboard Exercise

this module shows an image of a guitar neck and places a red dot on a random note and you have to name the note.

**Input Variables:**

*guitar neck view*
- vertical: guitar neck is positioned vertically with 1st fret at top of screen and 12th fret at bottom
- horizontal: guitar neck is positioned horizontally with 1st fret on left side of screen and 12th fret on right side of screen

*starting fret*

minimum fret you want to be quized on. if you want to be quizzed on the full fretboard choose 0.

*ending fret*

maximun fret you want to be quized on. if you want to be quizzed on the full fretboard choose 12.

*key*

key you want to be quizzed on. this will limit the notes you will be quized on to note in this key's diatonic scale. If you don't want to play within a certain key you can leave it blank (coming soon).

*strings*

strings you want to be quizzed on. if you want to be quizzed on the full fret board you need to select all of the strings.

## General Music Quizzes

This module offers a varriety of command line general music quizzes. All answers should be in capital letters seperated by commas (no spaces)

**Input Variables:**

*topics*
- chords: you are given a chord and you need to list the notes in that chord
- diatonic scales: you are given the key and need to list the diatonic scale (eg A Major: A,B,C#,D,E,F#,G#)
- pentatonic scales: you are given the key and need to list the pentatonic scale (eg A Major: A,B,C#,E,F#)
- modes: you are given a key and a mode and you need to list the scale (eg A Dorian: A,B,C,D,E,F#,G)

*difficulty*

for the chords topic, there is a difficulty variable you can set
1. easy: you will only be quized on major & minor chords with 6th and 7th chord extensions
2. medium: you will also be quizzed on sus chords and 9th chords
3. hard: you will be quizzed on all other chords including augmented, sharp 9ths, 11ths, and 13ths 

## Guitar Ear Training

*topics*
- pitch matching: choose notes you want to be quized on, a voicing of that note will play and you need to find a note on your fret board
- pitch training: choose notes to be quizzed on a guess which note it is
- interval training: choose intervals to be quizzed on and guess what the the interval is. you can play the two notes together or seperately
