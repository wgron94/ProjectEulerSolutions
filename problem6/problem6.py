import math
from timeit import default_timer as timer

# Problem statement: Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.?

start = timer()
squareOfSum = 0
sumOfSquares = 0
for i in range( 1, 101 ):
    squareOfSum += i
    sumOfSquares += math.pow( i, 2 )

squareOfSum = math.pow( squareOfSum, 2 )
diff = math.fabs( sumOfSquares - squareOfSum )
end = timer()

print( f"""The difference between the sum of the squares of the first one
           hundred natural numbers and the square of the sum: {diff}""" )
print( f"The solution time took {end-start}s" )

