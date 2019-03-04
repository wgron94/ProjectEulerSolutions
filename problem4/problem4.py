import math
from timeit import default_timer as timer

def is_palindrome( number ):
    string_value = str( number )
    length = len( string_value )
    i = 0
    while i < length / 2:
        if string_value[i] != string_value[length-1-i]:
            return False
        i += 1
    return True

start = timer()

# Problem statement: Find the largest palindrome made from the product of two
# 3-digit numbers

# There are 899 three digit numbers
# therefore the search space is 899 * 899 = 808,201 which is easily searchable

# First remove factors of 2
num1 = 100
num2 = 100
largest_palindrome = 0

for i in range( 100, 1000 ):
    for j in range( 100, 1000 ):
        product = i * j
        if is_palindrome( product ) and product > largest_palindrome:
            largest_palindrome = product
    
end = timer()

print( f"""The largest palindrome made from the product of two 3-digit numbers
           is {largest_palindrome}""" )
print( f"The solution time took {end-start}s" )
