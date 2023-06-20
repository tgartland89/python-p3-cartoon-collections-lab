# add this to clear the final tests for find_the_cheese 

CHEESES = ["camembert", "gouda", "cheddar"]

def roll_call_dwarves(dwarf_list):

    i= 1
    for name in dwarf_list:
        print(f'{i}. {name}')
        i += 1

# to pass this fail- first pass dwarf_list trhough roll_call:
#  i = 1, 
# for name in dwarf_list, 
# print (f'{i}. {name}')
#  i +=1 
#   
# FAILED Module cartoon_collections.py prints out the 7 dwarfs in a numbered list 
# - AssertionError: assert '' == '1. Dopey\n2....n3. Bashful\n'

def summon_captain_planet(planeteer_calls):

    return [f'{call.title()}!' for call in planeteer_calls]

# to pass the 2 for summon_cap:

# first pass planeteers_calls trhough summon_cap
# return [f'{call,title()}!' for call in planeteer_calls] 

# FAILED Module cartoon_collections.py returns true if any calls are longer than 4 characters 
# - TypeError: long_planeteer_calls() takes 0 positional arguments but 1 was given
# FAILED Module cartoon_collections.py returns false if all calls are 4 characters or less 
# - TypeError: long_planeteer_calls() takes 0 positional arguments but 1 was given
 

def long_planeteer_calls(words):

    for word in words:
        if len(word) > 4:
            return True

# adding this will clear first planeteer_long
# passing words throuhg long_planeteers
# for word in words:
# if len(word) > 4:
#return True

# FAILED Module cartoon_collections.py returns true if any calls are longer than 4 characters - 
# AssertionError: assert None == True
        
# adding return False will clear this fail for long_planeteers:
# FAILED Module cartoon_collections.py returns false if all calls are 4 characters or less 
# - AssertionError: assert None == False
    return False
              
def find_the_cheese(foods):

# # passing foods in to find_the_cheese clears the first fail:
# # FAILED Module cartoon_collections.py returns the first element of the array that is cheese 
# # - TypeError: find_the_cheese() takes 0 positional arguments but 1 was given

    for food in foods:
        if food in CHEESES:
            return food

    return None

# adding this will clear the final error
# for food in foods:
# in food in CHEESES: (make sure CHEESES is added on top with the 3 cheeses)
# return food 
# return None 
# FAILED Module cartoon_collections.py returns the first element of the array that is cheese 
# - AssertionError: assert None == 'cheddar'


# NOTES for me: 

# These functions perform different tasks and help with organizing and manipulating data.

# The code defines a list of cheeses: camembert, gouda, and cheddar.

# There is a function called "roll_call_dwarves" that takes a list of dwarf names as input.
# It prints each dwarf's name along with a number indicating their position in the list.
# For example, it would print "1. dwarf_name1", "2. dwarf_name2", and so on.

# There is a function called "summon_captain_planet" that takes a list of words as input.
# It transforms each word to start with a capital letter and adds an exclamation mark at the end.
# For example, if the word is "fire," it would return "Fire!"

# There is a function called "long_planeteer_calls" that takes a list of words as input.
# It checks if any word in the list has more than four letters.
# If it finds such a word, it returns True.
# If none of the words have more than four letters, it returns False.

# There is a function called "find_the_cheese" that takes a list of foods as input.
# It checks if any food in the list matches one of the cheeses in the predefined cheese list.
# If it finds a match, it returns the name of the cheese.
# If none of the foods are cheese, it returns None.

# ************************************************************************************************

# def roll_call_dwarves():
#     pass

# def summon_captain_planet():
#     pass

# def long_planeteer_calls():
#     pass

# def find_the_cheese():
#     pass



# ****************************************************************************

# CHEESES = ["camembert", "gouda", "cheddar"]

# def roll_call_dwarves(dwarf_list):
    
#     i = 1
#     for name in dwarf_list:
#         print(f'{i}. {name}')
#         i += 1

# def summon_captain_planet(planeteer_calls):
    
#     return [f'{call.title()}!' for call in planeteer_calls]

# def long_planeteer_calls(words):
    
#     for word in words:
#         if len(word) > 4:
#             return True
    
#     return False

# def find_the_cheese(foods):
    
#     for food in foods:
#         if food in CHEESES:
#             return food

#     return None