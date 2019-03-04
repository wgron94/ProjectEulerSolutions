import math
from timeit import default_timer as timer
start = timer()

# Problem statement: What is the largest prime factor of the number 600851475143 ?
value = 600851475143
i = 2

while value % i == 0:
    value = value / i

i = 3
while value != 1:
    while value % i == 0:
        value = value / i
    i += 2 # Can add by 2 to only check odd numbers because we removed all factors of 2 already

i -= 2 # Remove the last 2 that was added
end = timer()

print( f"The largest prime factor of 600851475143 is {i}" )
print( f"The solution time took {end-start}s" )
