desserts = ['cake', 'cookie', 'cheesecake', 'kitkat']
fruit = ['apple', 'banana', 'kiwi', 'strawberry', 'dragonfruit']

def foods (var1, var2) :
	return print(var1 + var2)

foods(desserts, fruit)

print('cake', 'cookie', 'cheesecake', 'kitkat', 'apple', 'banana', 'kiwi', 'strawberry', 'dragonfruit')

#code reads from the top of the code to the bottom.
#So if we define a variable as something in line 1, then use the same varibale equal to something else 
# in line 2, it will print as whatever it is set as in line 2

price = 10
price = 20
print(price)

# a whole number is an intiger while a decimal is a floater or float

intiger = 99
floater = 9.9
print(intiger, floater)

#booleans are true or false statements.
#Python is a case sensitive language- boolenas need to use capital T and F for true and false.
#We use an underscore to separate multiple words in our variables.

is_this_a_cool_bool = True
print(is_this_a_cool_bool)

#inputs are wasy for users to interact with code in the terminal! Waits for the use to put in 
# data before responding
#note to put in extra space after the question so there is some room for the curser in the terminal.
#The space goes in between the last character and the end quote.

name = input('What is your name? ')
color = input('What is your favorite color? ')
print("hi " + name + "! " + color + ' is a great choice.')

#you can use conversions like int(), bool(), and float(), to more easily let your code interact
# whenever you use input, you will always get a string. So if you want number, you should alwasy convert
# it into an integer or a float

birthYear = input('What is your birth year?: ')
age = 2021 - int(birthYear)
print("You will turn", age, "this year")

weight = input('What is your weight in pounds? ')
wconvert = int(weight) / 2.205
print("you weigh ", wconvert, " kilograms")

#Ypu can use triple quotes to define a string for multiple lines"
email = '''
Hi Lindsey,

Good news, we're hiring you because your code looks so amazing.
See you on Monday.
'''
print(email)

#python strings are indexed starting at zero and counting up(when going from left to right)
#when going from right to left, they count down, with the last character being -1.
#We use square brackets for indexing

phrase1 = "welcome to the internet"
phrase2 = ['welcome', 'to', 'the', 'internet']
print(phrase1[0])
print(phrase1[-1])
print(phrase2[0])

#you can also print out multiple characters by using a colon. It excludes the last number.
#if you use the square brackets and do not include an end value, it will return everything to the end.
# if you just put end ending index, it assumes 0 is the first number.

print(phrase1[0:6])
print(phrase1[8:])
print(phrase1[:7])

#holes or formatted strings are wasy to set up strings that have blanks in them for values to be filled in.
#formatted strings are prefixed with an f and then use quotes. so variable =f''
#use curly braces for the places you want to insert information within the formatted strings

firstpet = "cats"
secondpet = 'dogs'
animals = 'lions, tigers, and bears'
pets = f'{firstpet} and {secondpet} make great pets while {animals} do not.'
print(pets)

#you can use methods to do a variety of things in your existing code
#varibale.find =() to find something within your code. It will give you the index number.
#In the find method, it will just give you the first time the character/ word is seen
#you can replace words in the same format. With ("origional string", "new string")

tonguetwister = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
print(tonguetwister.find("wood"))
print('chuck' in tonguetwister)
