"""
Author : Sumama Chhotani
Python Recursive Function - Vowel replacement program
Put your solution to the vowels function in this file

"""

def Vowel_replace(input):
   
    vowel_list = ["a","e","i","o","u"]
    
    #base case
    if len(input) == 0:
        return input
    
    #recursive case
    if len(input) > 0:
        if input[0] in vowel_list:
            str = "*" + Vowel_replace(input[1:])
            return str
        else: 
            str = input[0]+ Vowel_replace(input[1:])
            return str



def main():
    string = "vowels"
    print(Vowel_replace(string))

main()