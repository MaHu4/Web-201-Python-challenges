# A palindrome is a number/string that is same 
# forwards and backwards. 
# For example 545, 151, 34543, 343, 171, 48984 are palindrome. 
# A string like LOL, MADAM are also palindromes. 
# Write a function that takes an variable and returns 
# True or False if the variable is a palindrome.


# A string is a palindrome if the reverse of the string is the same as string.


# Method 1: 
    # Find reverse of string
    # Check if reverse and original are same or not.

def is_palindrome(var):
    var = str("") # makes all var a string --> returns also integers into string  
    return var == var[::-1]  # <object_name>[<start_index>, <stop_index>, <step>] -->  s[::-1] --> the object is going to slice every "step" index from the given start index, till the stop index (excluding the stop index) and returns it
    
# Method 2: 

def test_challenge_04_palindrome_number():
    assert is_palindrome(545) == True

def test_challenge_04_palindrome_string():
    assert is_palindrome('MADAM') == True  

def test_challenge_04_palindrome_string2 ():
    assert is_palindrome('madam') == True

def test_challenge_04_palindrome_string3 ():
    assert is_palindrome('MadaM') == True  

def test_challenge_04_no_palindrome_string():
    assert is_palindrome('maddam') == False  