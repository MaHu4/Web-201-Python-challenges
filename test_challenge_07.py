# Supermarket billing: Write a function in python that 
# takes a shopping list (dictionary of items and price) and returns the total.
# extension: apply discount accordingly:
# if total is greater than 50 Euros 5% discount.
# if total is greater than 60 Euros 6% discount.
# if total is greater than 70 Euros 7% discount and so on. 
# --> for each 10€ = 1% discount starting from 50€

def calculate_bill(shopping_list):
    # if not isinstance(shopping_list, float) or not isinstance(shopping_list, int):
    #     return "not calculable" 
    
    Total = []  
    for i in shopping_list:
        if isinstance(i, float):
            Total = sum(shopping_list[i])
    print(Total)
    
    return(Total)

def test_challenge_07_happy_case(): 
    shopping_list = {'apples':11.20, 'bananas':2.2, 'eggs':30.00}
    assert calculate_bill(shopping_list) == 43.4

# def test_challenge_07_happy_case_2 (): 
#     shopping_list = {'apples':11.20, 'bananas':2.2, 'eggs':30.00}
#     assert calculate_bill(shopping_list) == 43.4
