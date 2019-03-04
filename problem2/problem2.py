# Setup initial values
# fib_value tuple holds the n-2, n-1, n Fibonnaci number
max_value = 4E6
fib_value = [ 1, 2, 3 ]
even_fib_sum = 2


while fib_value[2] < max_value:
    if fib_value[2] % 2 == 0:
        even_fib_sum += fib_value[2]

    # Calculate next Fibonacci number
    next_fib_num = fib_value[2] + fib_value[1]
    fib_value[0] = fib_value[1]
    fib_value[1] = fib_value[2]
    fib_value[2] = next_fib_num
    print( f"Current Fibonacci values: {fib_value[0]}, {fib_value[1]}, {fib_value[2]}" )

print( f"The sum of even valued Fibonacci numbers less than 4E6 is {even_fib_sum}" );
