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

"""

#Display the welcome and options
print("Welcome to the formula calculator".center(71, "!"))
print("\nPlease choose one of the following to calculate:")
print(options)

#A list of valid choices for the corresponding programs to launch
optionalNums = [1, 2, 3, 4, 5, 6]

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

    #Launch a program based on the user choice
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

    #Ask the user if they would like to launch another program or exit?
    keepGoing = input("Would you like to run another program? (Y or N)\n-->")
    if (keepGoing.upper() == "Y"):
        print(options)
        continue
    elif (keepGoing.upper() == "N"):
        break
    else:
        break
