# Write a function in Python that accepts a list of 
# any length that contains a mix of non-negative 
# integers and strings. The function should return 
# a list with only the integers in the original 
# list in the same order.

from typing import Iterable


def extract_integers(mixed_list):
    integer_list = [] #empty list
    if isinstance(mixed_list, Iterable):
     for i in (mixed_list): # goes one by one through the list; in for-loops, variable in () must be iterable
     #    print(i)
        if isinstance(i, int): # ifinstance --> i = to be evaluate, int = type to be checked, here an integerx
             integer_list.append(i) # ask the integer_list to do an append, i.e. add an element to a list; in this case i = integer
    return integer_list 


def test_challenge_05_happy_case(): 
     assert extract_integers([1, 'apple', 2, 'banana',3, 4]) == [1,2,3,4]   

def test_challenge_05_sad_case_Null_input(): 
     assert extract_integers(None) == []    # None (=null in JS) = nothing

def test_challenge_05_emptyList(): 
     assert extract_integers([]) == [] 

def test_challenge_05_noInteger(): 
     assert extract_integers(['apple', 'banana']) == []  

def test_challenge_05_Float_case(): 
     assert extract_integers([1.5, 'apple', 2, 'banana',3, 4]) == [2,3,4]      