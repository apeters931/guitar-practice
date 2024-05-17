import guitar_note_quiz as guitar
import music_theory_quiz as theory

def main():
    flag = True
    while flag:
        choice = input("Type 1 for Guitar Note Quiz; Type 2 for Scale & Arpeggio Quiz: ")
        if choice == "1":
            guitar.main()
            flag = False
        elif choice == "2":
            theory.main()
            flag = False
        else:
            print('Input not accepted')

main()
