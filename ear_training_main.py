import interval_training as it
import pitch_matching as pm
import pitch_training as pt

def main():
    flag = True
    while flag:
        choice = input(
            "\nSelect what you would like to be quized on.\nA. Pitch Matching\nB. Pitch Training\nC. Interval Training\n\n"
        )
        if choice == "A":
            pm.main()
            flag = False
        elif choice == "B":
            pt.main()
            flag = False
        elif choice == "C":
            it.main()
            flag = False
        else:
            print('Input not accepted')
