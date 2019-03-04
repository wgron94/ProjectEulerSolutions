import math
from timeit import default_timer as timer

def calculate_prime_factors( number ):
    prime_factors = list()
    i = 2
    while number % i == 0: # Remove factors of 2 first
        number = number / i
        prime_factors.append( i )

    i = 3
    while number != 1:
        while number % i == 0:
            number = number / i
            prime_factors.append( i )
        i += 2 # Can add by 2 to only check odd numbers because we removed all factors of 2 already
    return prime_factors

def duplicates_removed( main_list, addition ):
    dup_removed_list = list()
    for i in prime_factors:
        if i in main_list:
            main_list.remove( i )
        else:
            dup_removed_list.append( i )
    return dup_removed_list

# Problem statement: What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

start = timer()
min_prime_factors = list()

for i in range( 2, 21 ):
    prime_factors = calculate_prime_factors( i )
    min_prime_factors += duplicates_removed( list( min_prime_factors ), prime_factors )

smallest_even_divisible = 1;
for i in min_prime_factors:
    smallest_even_divisible *= i
    
end = timer()

print( f"""The smallest positive number that is evenly divisible by all of the
           numbers from 1 to 20 is {smallest_even_divisible}""" )
print( f"The solution time took {end-start}s" )

