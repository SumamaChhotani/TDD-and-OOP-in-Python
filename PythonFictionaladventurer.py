"""
Author : Sumama Chhotani
Pyhton  Adventurer class defintion (and tests!) in this file
"""

class Adventurer:
    def __init__(self, name, favorite_quest, favorite_food, favorite_equipment):
        """
        Construct a new character
        Parameters: Name, fav things to do, fav food, fav eqip- all strings)
        """
        self.name = name
        self.quest_fav = favorite_quest
        self.food_fav = favorite_food
        self.equipment_fav = favorite_equipment

        self.quest_acc = 0
        self.food_acc = 0
        self.equipment_acc = 0


    def __str__(self):
        """ Create a string representation"""
        return "%s likes doing %s when eats %s  and has %s" % (self.name, self.quest, self.food, self.equipment)

    def get_name(self):
        return self.name

    
    def quest(self):
        
        if self.food_acc <= 0:                       #adventurer cannot go on a quest if they haven’t eaten
            print("%s needs to eat before %s" % (self.name, self.quest_fav))

        elif self.food_acc > 0:                        #reduce the food by 1
            self.food_acc = self.food_acc - 1
            self.quest_acc = self.quest_acc +1 #update the Adventurer’s state
            print("%s is %s" % (self.name , self.quest_fav)) #prints

    
    
    def eat(self):
        if self.food_acc <= 1:                                  #if character is hungry or has eaten food only once
            self.food_acc = self.food_acc + 1                   # increases the food acc by 1- updates  
            print("%s ate some %s" % (self.name , self.food_fav)) # print the message

        elif self.food_acc == 2 :                                  #if character has already eaten twice
            print("%s has already eaten too much" % (self.name)) # says its eaten too much and doesnt adds
        
    
    def shop(self):
        self.equipment_acc = self.equipment_acc + 1
        print("%s bought %s" % (self.name, self.equipment_fav))

    def rest(self):
        while self.food_acc >= 0:
            self.food_acc = self.food_acc -1

        while self.quest_acc >= 0:
            self.quest_acc = self.food_acc -1 

        print("%s is resting" %(self.name))


    def status(self):
        if self.food_acc == 0:
            food_state = "hungry"
        elif self.food_acc == 1:
            food_state = "fed"
        elif self.food_acc == 2:
            food_state = "Well-fed"

        if self.quest_acc == 0:
            quest_state = "wants to be "
        elif self.quest_acc == 1:
            quest_state = "contented with"
        elif self.quest_acc == 2:
            quest_state = "over joyed with"

        if self.equipment_acc == 0:
            equipment_state = "could use some"
        elif self.equipment_acc == 1:
            equipment_state = "has some"
        elif self.equipment_acc >= 2:  #no such thing as max in this case
            equipment_state = "has load of"

        print("%s is %s, %s %s and %s %s" %(self.name,food_state,quest_state,self.quest_fav,equipment_state,self.equipment_fav))

def main():
    rich = Adventurer("Rich", "doing the crossword", "pizza", "pens")  #test
    rich.eat() #test
    rich.eat() #test
    rich.quest() #test
    rich.quest() #test
    rich.status() #test

if __name__ == "__main__":
    main()