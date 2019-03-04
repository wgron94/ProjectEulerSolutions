sum_of_multiples = 0;

for i in range( 1, 1000 ):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_multiples += i

print( f"The sum of all multiples of 3 or 5 below 1000 is {sum_of_multiples}" );
