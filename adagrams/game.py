import random
    #Your first task is to build a hand of 10 letters for the user. To do so, implement the function draw_letters in game.py. This method should have the following properties:
"""
No parameters
Returns an array of ten strings
Each string should contain exactly one letter
These represent the hand of letters that the player has drawn
The letters should be randomly drawn from a pool of letters
This letter pool should reflect the distribution of letters as described in the table below
There are only 2 available C letters, so draw_letters cannot ever return more than 2 Cs -- no sets then, look for case sensativity
Since there are 12 Es but only 1 Z, it should be 12 times as likely for the user to draw an E as a Z
Invoking this function should not change the pool of letters
Imagine that the user returns their hand to the pool before drawing new letters

"""
#in letter out qty
letter_dict = {
"A" : 9,	
"B" : 2,
"C" : 2,	
"D" : 4,	
"E" : 12,	
"F" : 2,	
"G" : 3,	
"H" : 2,	
"I" : 9,
"J" : 1,	
"K" : 1,	
"L" : 4,
"M" : 2,
"O": 8,
"P": 2,
"Q": 1,
"R": 6,
"S": 4,
"T": 6,
"U": 4,
"V": 2,
"W": 2,
"X": 1,
"Y": 2,
"Z": 1,
}


    pass

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass