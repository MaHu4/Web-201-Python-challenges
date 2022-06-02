# Write a function in python that 
# takes an array of numbers and returns a
# sum of the square of all the numbers in the array.


#Solution 1:

def sum_of_squares(array_of_numbers):
    if not isinstance(array_of_numbers, list):
        return "Not a list"

    sum = 0 # variable to store the sum later, initialized with 0; needs to be initialized because we have the sum on the right side of = in line 15
    for i in array_of_numbers:
        if isinstance(i, int):
            sum = (i * i) + sum  # goes through array elements in a loop: (1+1)+0 --> sum = 1 --> (2*2)+1 --> sum = 5
        if not isinstance(i, int):
            return("No integer")
    return (sum)

#Solution 2: wirth sum()-function

def sum_of_squares(array_of_numbers):
    
     if not isinstance(array_of_numbers, list): # there are no arrays in phyton; lists are used instead
        return "Not a list"
    
     list_of_multiplications = [] #sum-function in line 34 needs a list; here we create a variable with an empty list; important to be outside the for-loop

     for i in array_of_numbers:
          if isinstance(i, int) or isinstance(i, float):
           list_of_multiplications.append(i**2) # adds the single squared elements in a list by means of append; (i*i) works as well
          else:
               return("Not a number")
     Sum = sum(list_of_multiplications)
     return (Sum)


def test_challenge_06_happy_case(): 
     assert sum_of_squares([1,2,3,4]) == 30

def test_challenge_06_happy_case_2(): 
     assert sum_of_squares([7,1,50]) == 2550

def test_challenge_06_happy_float_case(): 
     assert sum_of_squares([1.0,2,3,4]) == 30

def test_challenge_06_happy_case_3(): 
     assert sum_of_squares(["a", "b", "c", "d"]) == "Not a number"

def test_challenge_06_happy_case_4(): 
     assert sum_of_squares(["aloha"]) == "Not a number"

def test_challenge_06_sad_case(): 
     assert sum_of_squares("") == "Not a list"    
