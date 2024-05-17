import guitar_fretboard_exercise as gnq
import music_quizzes as mq
import ear_training_main as et

def main():
    flag = True
    while flag:
        choice = input(
            "\nType 1 for Guitar Fretboard Exercise\nType 2 for General Music Quizzes\nType 3 for Guitar Ear Training\n\n"
        )
        if choice == "1":
            gnq.main()
            flag = False
        elif choice == "2":
            mq.main()
            flag = False
        elif choice == "3":
            et.main()
            flag = False
        else:
            print('Input not accepted')

main()
