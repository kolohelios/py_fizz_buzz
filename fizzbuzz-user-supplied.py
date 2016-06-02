import sys

# Check the command line argument; if there's no value, make sure we get one
# from user input; if it's invalid, we will let the user know.
try:
    max_value = int(sys.argv[1])
except IndexError:
    invalidValue = True
except ValueError:
    print('You did not pass a valid argument (a positive whole number).\n')
    invalidValue = True
else:
    invalidValue = False
    
# If we didn't get a valid command line argument, we'll use a loop to continue
# to prompt the user for a value until we get a valid value.
while invalidValue:
    input_value = input('Please enter the maximum value (a positive whole number) to fizz buzz: ')
    try:
        max_value = int(input_value)
    except ValueError:
        print('That was an invalid entry.\n')
    else:
        invalidValue = False

print('Fizz buzz counting up to {0}'.format(max_value))

# We have to add 1 to max_value to because our range is open:closed;
# otherwise, we would miss our max value.
for n in range(1, max_value + 1):
    if (n % 3 == 0) and (n % 5 == 0):
        print('fizz buzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)