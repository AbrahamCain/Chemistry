#A launcher to run your programs in a nicer looking way
import os
import sys

options = """
1.  Density given Mass and Volume
2.  Volume given Density and Mass
3.  Mass given Volume and Density

4.  Work given Force and Distance
5.  Force given Distance and Work
6.  Distance given Work and Force

7.  Atoms from Grams
8.  Atoms from Moles
9.  Moles from Atoms
10. Moles from Grams
11. Grams from Atoms
12. Grams from Moles

13. Find the moles or grams needed to ballance the reaction
"""
print("Welcome to the formula calculator".center(71, "!"))
print("\nPlease choose one of the following to calculate:")
print(options)

optionalNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Keep asking to run programs until the user is done
while True:
    try:
        choice = int(input("Choose a program by number -->"))
    except:
        while True:
            print("Invalid Choice. Valid choices are a number from 1 to 6.")
            choice = input("try again -->")
            if (choice.isnumeric() and int(choice) in optionalNums):
                break

    if (choice == 1):
        os.system("python density.py")
    elif (choice == 2):
        os.system("python volume.py")
    elif (choice == 3):
        os.system("python mass.py")  
    elif (choice == 4):
        os.system("python work.py")  
    elif (choice == 5):
        os.system("python force.py")  
    elif (choice == 6):
        os.system("python distance.py")
    elif (choice == 7):
        os.system("python atomsFromGrams.py") 
    elif (choice == 8):
        os.system("python atomsFromMoles.py")
    elif (choice == 9):
        os.system("python molesFromAtoms.py")
    elif (choice == 10):
        os.system("python molesFromGrams.py")
    elif (choice == 11):
        os.system("python gramsFromAtoms.py")
    elif (choice == 12):
        os.system("python gramsFromMoles.py")
    elif (choice == 13):
        os.system("python molesNeeded.py")


    keepGoing = input("Would you like to run another program? (Y or N)\n-->")
    if (keepGoing.upper() == "Y"):
        print(options)
        continue
    elif (keepGoing.upper() == "N"):
        break
    else:
        break
