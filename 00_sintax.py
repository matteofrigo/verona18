"""
PRINT AND STRINGS
"""
print('Hello, world!')
print('')
print('I just skept a line')
print('but I could skip more of them in this way. Check it here below!\n\n\n\n')
print('You see? It was easy.\n')

next_string = 'The "print" function accepts a predefined string as input.'
print(next_string)
print('\nPrinting is very important.\n\tDo\tit\tproperly!')

"""
IF STATEMENT
"""
print_more_stuff = True
print('')
if print_more_stuff:
    print("I'm printing something inside an 'if' statement!")
else:
    print("Ok, you didn't want to print more stuff, but I don't really care \
          what you wanted to do.")

"""
FOR STATEMENT
"""
# A "for" statement works like this:
for k in range(0,10):
    # do something
    print(k)

mystring = '\nI can print the single characters of a string'
print(mystring)
for character in mystring:
    print(character)

"""
LISTS
"""
# Here I have a list
mylist = [1,2,35,57,342,45,345,35,65,865,9,47,56]
print(mylist)
# It is an iterable object, which means that I can write a for loop on it
for k in mylist:
    print(k)
# I can take only its first two elements
print(mylist[:2])
# Or the two last ones
print(mylist[-2:])
# Or one every three elements
print(mylist[::3])

"""
FUNCTIONS
"""
# This function returns a value
def compute_double(input_number):
    twice_the_input = 2*input_number
    return(twice_the_input)

mynumber = 2018
its_double = compute_double(mynumber)
print(str(mynumber)+' times 2 is '+str(its_double))

# This function returns multiple values
def some_operations(input_number = 13):
    twice = compute_double(input_number)
    third_power = input_number**3
    minus_one = input_number - 1
    division_by_three = input_number / 3
    another_division_by_three = input_number / 3.0
    integer_division_by_three = input_number // 3
    return twice, third_power, minus_one, \
           division_by_three, another_division_by_three, \
           integer_division_by_three

tuple_with_the_output = some_operations(mynumber)
print(tuple_with_the_output)
print('The default output is')
print(some_operations())
myinput = 42
print('The output for input=%02d is' % myinput)
print(some_operations(myinput))
