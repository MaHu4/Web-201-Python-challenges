# Create a function in Python that accepts a single word and 
# returns the number of vowels in that word. 
# In this function, only a, e, i, o, and u 
# should be counted as vowels — not y.

def count_vowels(word):
    count = 0 #new variable starting from 0
    for each_character in word:
        if each_character == 'a' or each_character == 'e' or each_character == 'i' or each_character == 'o' or each_character == 'u': # : closes the if-statement
            count = count + 1 
    print(count)
    #RETURN STATEMENT --> must be always the last line; ends the function
    return count # returns count outside of the function to get the result; otherwise, the function returns NONE
  

def test_challenge_01_happy_case(): 
     assert count_vowels('Kaleidoscope') == 6   
     # test needs to start with test_; afterwards new name can be given
     #we can change the word Kaleidoscope by any other word

# add test cases
def test_emty_case(): 
     assert count_vowels('') == 0 