# https://www.interviewcake.com/question/python/product-of-other-numbers
from functools import reduce

def compute_product(input_array):
    # Given an input array, for each index finds a product of every integer except the integer at that index
    # Get the lists of all other integers except 'us'
    other_integers = [[y for y in input_array if not y == input_array[i]] for i, _ in enumerate(input_array)]
    # Use the reduce function to compute the product
    return [reduce((lambda x,y: x*y), array) for array in other_integers]


# Desired output: [84, 12, 28, 21]
test_array = [1, 7, 3, 4]
print(compute_product(test_array))
