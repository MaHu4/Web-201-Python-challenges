# Write a function in Python that accepts a list of 
# any length that contains a mix of non-negative 
# integers and strings. The function should return 
# a list with only the integers in the original 
# list in the same order.

import re


# def extract_integers(mixed_list):
#     mixed_list = [] # list of any lenth
#     for i in mixed_list:
#         if i == int(i) # abd() lgives a positive value of an integer/float in return


def extract_integers(mixed_list):
    mixed_list = []
    import re
    res = re.findall('[-+]?\d+', mixed_list) # Segregate Positive and Negative Integers using regex
    return str(res)



def test_challenge_05_happy_case(): 
     assert extract_integers([1, 'apple', 2, 'banana',3, 4]) == [1,2,3,4]   