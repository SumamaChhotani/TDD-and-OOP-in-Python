"""
Author : Sumama Chhotani
15th Nov 2022
Python Sorting Program

"""

# import the library for this lab
from food_access_lab import *

#def load_file():
#This function opens our files,reads it and converts string into an appended list of objects which we refer 
#throughout our program.
#Parameters : None - (I could have load the file through main, and using it a parameter, but found it more easy this way)
#Returns : a List of Objects 
def load_file():
  list = []
  file_obj = open("/data/cs21/food_access/food_access.csv", "r")
  raw_data = file_obj.read()
  lines = raw_data.splitlines()
  for w in lines:
    record = FoodAccessRecord(w)
    list.append(record)
  return list


#This function asks the user for the search preference and validates input. IF user types in invalid input, 
#it reprompts the user to retype correct one. It returns a choice (string) that will be used in calling out other fucntions.
#Parameters : None
#Returns : user selection -string 
def get_choice_initial():
  print("Please select one of the following choices:")
  print("1. Filter records by state name")
  print("2. Filter by Population")
  print("3. Sort by state name")
  print("4. Sort by total population")
  print("5. Reset list to all records")
  print("0. Quit")
  print("")
  User_selection = (input("Choice?"))
  while User_selection != "1" and User_selection != "2" and User_selection != "3" and User_selection != "4" and User_selection != "0" and User_selection != "5":
    print("Invalid choice, try again!")
    User_selection = (input("Choice?"))

  return User_selection


# def search_by_state_linear:
#This Functions take our list as input, and uses linear search to accumulate data as per state in our empty list
# Paramenter : Input from user(string); Data - list
# Return : Accumulator - List  
def search_by_state_linear(input_from_user,data):
  user_input = input_from_user                     #did this extra step for clarity 
  Accumulator_list = []
  for i in data:
    if i.get_state().lower().startswith(user_input):  #.lower() converts it into lowercase
      Accumulator_list.append(i)
  return Accumulator_list
 


def min_max_input_validation():  #before filtering by Min Max
    #This Functon does two things : Asks user for min max value, and validates it
    # Parameters : None
    #Returns - A list of validated Min Max value inputed by user
    MinPopulation = input("Minimum Population?")   
    while MinPopulation.isdigit() == False:  #checks for integer - no float/string
      print("Error: minimum population must be a positive integer; please try again!")
      MinPopulation = input("Minimum Population?")
    while int(MinPopulation) < 0:  #checks for negative ints.
      print("Error: minimum population must be a positive integer; please try again!")
      MinPopulation = input("Minimum Population?")
    
    MaxPopulation = input("Maximum Population?")   
    while MaxPopulation.isdigit() == False:  #checks for integer - no float/string
      print("Error: Maximum population must be a positive integer; please try again!")
      MaxPopulation = input("Maximum Population?")
    while int(MaxPopulation) < 0:  #checks for negative ints.
      print("Error: Maximum population must be a positive integer; please try again!")
      MaxPopulation = input("Maximum Population?")

    list = [MinPopulation, MaxPopulation]
    return list


def search_by_threshold(Min, Max, data):
  #This function does linear search by threshold
  #Para : Min (str), Max (str), Data (list)
  #Returns : List 

    Minimum = int(Min) #converts str into int
    Maximum = int(Max)
    Accumulator_list = []
    for i in data:
      if i.get_population() > Minimum and i.get_population() <Maximum: 
        Accumulator_list.append(i)
    return Accumulator_list


def bubble_sort(lst):    
    #Sorts the list using Bubble sort. 
    #Mutates the list so there is no return value.
    #Parameter: #lst (list): a list of objects
    #Return: None
    #Side Effects : List is mutated
    n = len(lst)
    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j].get_state() > lst[j+1].get_state():
                lst[j], lst[j+1] = lst[j+1], lst[j]


def selection_sort(lst):
    #Sorts the list using selection sort. 
    #Mutates the list so there is no return value.
    #Parameter: #lst (list): a list of objects
    #Return: None
    #Side Effects : List is mutated

    n = len(lst)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if lst[j].get_population() < lst[min_index].get_population():
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]


#This Function takes list as input, and print it accordingly using string formatiing- each member of the list
#Parameter : list - type list
#return : Nothing 
def print_val(list):
    print("================================================================================") #Heading lines of table
    print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( "County", "State", \
      "Total Pop", "LFA Pop", "Income", "Senior", "Vehicle" ) )
    print("--------------------------------------------------------------------------------")
    for i in list:
      County = i.get_county()
      State = i.get_state()
      Total_Pop = i.get_population()
      LFA_Pop = i.get_people(1)
      Senior = i.get_seniors(1)
      Income = i.get_low_income(1)
      Vehicle = i.get_vehicle_access(1)
      
     
      print("| %15s | %12s |%9s| %7s| %6s | %6s | %7s|" % ( County[0:15], State[0:12], \
      Total_Pop, LFA_Pop, Income, Senior, Vehicle ))
      print("--------------------------------------------------------------------------------")
    

#runs the Program
def main():
  data_list = load_file() #calls the function that loads file and returns list of objects
  reset_data = data_list.copy() # makes a copy of original data list- for reset functionality
  
  while True:
    initial_choice = get_choice_initial()    # gets a string of 1,2,3,4,5
    if initial_choice == "0": #exit
      print("Goodbye!")
      break

    elif initial_choice == "5": #reset
       data_list = reset_data #Resets the list by making it the origional copied version "reset data"
       print()
       print("Resetting list to contain all records...")
       print()
  
   
    elif initial_choice == "2":  #filtering by min/max pop
       list_of_min_max = min_max_input_validation() #ask user for min/max and validates
       MinValue = list_of_min_max[0]
       Maxvalue = list_of_min_max[1]
       
       population_list_result  = search_by_threshold(MinValue, Maxvalue ,data_list) #linear filter                 
       
       if population_list_result != []: 
        data_list = population_list_result #makes this new list the data now
        print_val(population_list_result)
       else:
          print("No Records Found")
    
    
    elif initial_choice == "1": #filtering by state name alphabatecially
      User_input = input("State name (or prefix)?")
      User_input = User_input.lower()                             #converts into lower                  
      state_list_result = search_by_state_linear(User_input,data_list)
      if state_list_result != []:
        data_list = state_list_result #makes this new list of data now
        print_val(state_list_result)
      else:
        print("No Record Found")
    
    
    elif initial_choice == "4": # Sorts By Population using Selection Sort
      selection_sort(data_list)
      print_val(data_list)

    else:                     #Sorts by State using Bubble Sort
      bubble_sort(data_list)
      print_val(data_list)

main()
