# Create a Python function that accepts a string. 
# The function should return a string, with each 
# character in the original string doubled. 
# If you send the function "now" as a parameter, 
# it should return "nnooww," and if you send "123a!", 
# it should return "112233aa!!".


# # Solution 1: with for loop (by looping through each character and appending it to a list, which is then joined and returned at the end):
# def duplicate_characters(string):
#      double = []
#      for i in string:
#           double.append(i+""+i)
#      print(double)
#      return "".join(double)


#Solution 2: with for-loop
# def duplicate_characters (string):
#     outstring = ""
#     for char in string:
#         outstring = outstring + char + char
#     return outstring


#Solution 3: integrated for-loop 1:

# def duplicate_characters (word):
#     return "".join([i+''+i for i in word]) 

#         # .join(...) glues everything in (...) together into one piece without spaces, i.e. ''.join('a', 'b', 'c') will return 'abc'.
#         # i+''+i duplicates each character
#         # for loop - goes over every element in text

# Solution 4: integrated for-loop 2:

# def duplicate_characters (s):
#     return ''.join(a * 2 for a in s)
     
#      # .join(...) glues everything in (...) together into one piece without spaces, i.e. ''.join('a', 'b', 'c') will return 'abc'.
#      # [a * 2 ...] - repeats a/each characte 2 times
#      # for loop - goes over every element in text



#Solution 5: integrated for-loop 3

def duplicate_characters (string):
    return ''.join([a+a for a in string])

# Tests:

def test_challenge_02_case_1(): 
     assert duplicate_characters('now') == 'nnooww'
     # --> passed

def test_challenge_02_case_2(): 
     assert duplicate_characters('123a!') == '112233aa!!'
     # --> passed

def test_camelCase_case():
     assert duplicate_characters('Iam') == 'IIaamm' 
     # --> passed

def test_space_case():
     assert duplicate_characters('I am') == 'II  aamm' 
     # --> passed

 # Source for solutions 1,3,4 see: https://ao.ms/how-to-double-characters-in-python/, 
 # Source for solutiona 2,5, see: https://stackoverflow.com/questions/23545855/character-repeating-in-a-string




