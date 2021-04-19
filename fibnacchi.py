### --------------------Fibonacci Number -----------------------------####

#Function to calculate Fibonacci Number
def fibonacci(number):
    if number <=1:
        return number
    else:
        return fibonacci(number-1)+fibonacci(number-2)

# Enter Input for Fibonacchi Series:
number=int(input('Enter a Positive Number  : '))

if number <=0:
    print('Please enter a Positive Number !!! ')
else:
    print('############################\n','Fibonacchi Series is :')
    for i in range(number):
        print(fibonacci(i), end=' ')
    print('\n############################')