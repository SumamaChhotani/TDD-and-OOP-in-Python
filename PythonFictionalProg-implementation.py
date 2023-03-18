"""
Implemention of the menu-driven team.py program in this file
Author: Sumama CHhotani
Date: Fri, 2nd Dec 2022
"""
from adventurer import*


"""
This fucnction Prints menu list, ask for user input, validates and returns user input
Para: None
Returns : Str of a number
"""
def menu():
    print("Main Menu:")
    print("1. Report the status of the adventurers")
    print("2. Recruit a new adventurer")
    print("3. Take an adventurer on a quest")
    print("4. Feed an adventurer")
    print("5. Shop for an adventurer")
    print("6. Rest for the night")
    print("0. Quit")
    menu_choice = input("Enter Selection ")
    
    
    while not (menu_choice.isdigit() and int(menu_choice)<= 6 and int(menu_choice) >= 0): #handles invalid input
        print("Invalid selection, please try again.")
        menu_choice = input("Enter Selection ")
    return menu_choice
    

"""
This funtciton prints the status of Objects 
Para : list of Object
Returns : None
(Prints)
"""
def report_status(listOfObjects):
    for i in listOfObjects:
        i.status()
    if len(listOfObjects) == 0:
        print("No adventurers on your team. Try adding one!")


"""
This funtciton recruits a new character
Para : None
Returns : Object (Class)
"""
def recruit_new():
    Adv_name = input("Adventurer's name: ")
    Favorite_quest= input("Favorite quest: ")
    Favorite_Food = input("Favorite food: ")
    Favorite_equipment = input("Favorite equipment: ")
    
    return Adventurer(Adv_name, Favorite_quest, Favorite_Food, Favorite_equipment)  


"""
This funtciton makes the character go on a quest
Para : list of Object
Returns : None
(Prints)
"""
def quest(ListOfObjects):
    if len(ListOfObjects) != 0:
        print("Here are the adventurers on your team:")
        
        for i in range(len(ListOfObjects)):
            print(str(i+1)+ ". " + ListOfObjects[i].get_name())

        Choice = input("Choose an adventurer: ")
        
        while not (Choice.isdigit() and int(Choice) >= 1 and int(Choice) <= len(ListOfObjects)): #handles invalid input
            print("Invalid selection, please try again.")
            Choice = input("Choose an adventurer: ")
        

        object = ListOfObjects[int(Choice)-1]
        object.quest()
    else:
        print("No adventurers on your team. Try adding one!")



"""
This funtciton makes the character eats
Para : list of Object
Returns : None
(Prints)
"""
def feed(ListOfObjects):
    if len(ListOfObjects) != 0:
        print("Here are the adventurers on your team:")
        
        for i in range(len(ListOfObjects)):
            print(str(i+1)+ ". " + ListOfObjects[i].get_name())

        Choice = input("Choose an adventurer: ")
        
        while not (Choice.isdigit() and int(Choice) >= 1 and int(Choice) <= len(ListOfObjects)): #handles invalid input
            print("Invalid selection, please try again.")
            Choice = input("Choose an adventurer: ")
        


        object = ListOfObjects[int(Choice)-1]
        object.eat()
    else:
        print("No adventurers on your team. Try adding one!")

"""
This funtciton makes the character shop
Para : list of Object
Returns : None
(Prints)
"""
def Shop(ListOfObjects):
    if len(ListOfObjects) != 0:
        print("Here are the adventurers on your team:")
        
        for i in range(len(ListOfObjects)):
            print(str(i+1)+ ". " + ListOfObjects[i].get_name())

        Choice = input("Choose an adventurer: ")
        
        while not (Choice.isdigit() and int(Choice) >= 1 and int(Choice) <= len(ListOfObjects)): #handles invalid input
            print("Invalid selection, please try again.")
            Choice = input("Choose an adventurer: ")
        
        


        
        object = ListOfObjects[int(Choice)-1]
        object.shop()
    else:
        print("No adventurers on your team. Try adding one!")

"""
This funtciton makes all the character rest
Para : list of Object
Returns : None
(Prints)
"""
def rest(ListOfObjects):
    if len(ListOfObjects) != 0:
        for i in ListOfObjects:
            i.rest()
    else:
        print("No adventurers on your team. Try adding one!")


#MAin Fuction : Runes the entire program
def main():
    lst_objects = []   #list of adventurers 
    while True:
        choice = int(menu())     #since  my menu returns output in str, it necessary to convert into int

        if choice == 1:
            report_status(lst_objects)

        elif choice == 2:
            new_adv = recruit_new()
            lst_objects.append(new_adv)

        elif choice == 3:
            quest(lst_objects)
        elif choice == 4:
            feed(lst_objects)
        elif choice == 5:
            Shop(lst_objects)

        elif choice == 6:
            rest(lst_objects)

        elif choice == 0:
            print("GoodBye!")
            quit()


main()