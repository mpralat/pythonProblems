# https://www.interviewcake.com/question/python/highest-product-of-3
# Given a list of integers, find the highest product you can get from three of the integers.
from itertools import combinations
from functools import reduce


def compute_the_highest_product(input_array, number):
    # inefficient way: 3 loops
    possible_combinations = [list(x) for x in combinations(input_array,number)]
    # Zipping only because we want to get the values as well, not just the product
    result_tuples = list(zip([reduce((lambda x,y: x*y), combination) for combination in possible_combinations], possible_combinations))
    return max(result_tuples, key=lambda  x: x[0])



test_example = [-10, -10, 1, 2, 3]
# Expected result = 300
print(compute_the_highest_product(test_example,3))