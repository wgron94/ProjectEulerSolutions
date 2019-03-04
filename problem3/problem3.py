import math
from timeit import default_timer as timer
start = timer()

# Problem statement: What is the largest prime factor of the number 600851475143 ?
value = 600851475143
i = 2
max_prime_factor = math.sqrt( value )

# First remove factors of 2
while value % i == 0:
    value = value / i

i = 3
while i < max_prime_factor:
    if value / i == 1:
        break # At this point we have reached the end of the factorization
    while value % i == 0:
        value = value / i
    i += 2 # Can add by 2 to only check odd numbers because we removed all factors of 2 already
end = timer()

print( f"The largest prime factor of 600851475143 is {i}" )
print( f"The solution time took {end-start}s" )
