# A palindrome is a number/string that is same 
# forwards and backwards. 
# For example 545, 151, 34543, 343, 171, 48984 are palindrome. 
# A string like LOL, MADAM are also palindromes. 
# Write a function that takes an variable and returns 
# True or False if the variable is a palindrome.


# A string is a palindrome if the reverse of the string is the same as string.


# Method 1: 

def is_palindrome(var):
    var = str(var) # makes all var a string --> returns also integers into string  
    return var == var[::-1]  # slice operation object_name[start_index : stop_index : step] -->  var[::-1] --> the object is going to slice every "step" index from the given start index, till the stop index (excluding the stop index) and returns it
    


# Method 2: boolean using the inbuilt function to reverse a string

# def is_palindrome(var):
#     # var = str("") # error: produces blank strings; it overrides a variable which shoul dbe avoided
#     str_var = str(var)
#     rev = ''.join(reversed(str_var))

#     if (str_var == rev):
#         return True
#     else:
#         return False
     

def test_challenge_04_palindrome_number():
    assert is_palindrome(545) == True #  passed

def test_challenge_04_palindrome_string():
    assert is_palindrome('MADAM') == True # passed

def test_challenge_04_palindrome_string2 ():
    assert is_palindrome('madam') == True # passed

def test_challenge_04_palindrome_string3 ():
    assert is_palindrome('MadaM') == True  # passed

def test_challenge_04_palindrome_string4 ():
    assert is_palindrome('MaddaM') == True  # passed

def test_challenge_04_no_palindrome_string():
    assert is_palindrome('HELLO') == False  # pass

# source of inspiration for Method 1 + 2: https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/