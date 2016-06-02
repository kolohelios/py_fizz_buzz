max_value = 100

print('Fizz buzz counting up to {0}'.format(max_value))

for n in range(1, max_value):
    if (n % 3 == 0) and (n % 5 == 0):
        print('fizz buzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)