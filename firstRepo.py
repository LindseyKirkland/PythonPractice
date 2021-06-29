#arithmetic operators are addition(+), subtraction(-), multiplication)*), and division(/ or //)
#for division, / will give you a float number and // will round for an intiger
#% returns the remainder of the division.
#to perform ecponential operations, use ** 

print(10%3)
print(2**3)
print(10//3)

#we can also use augmented assigment operators if we want to change/ redefine an intiger
#python also understand order of operations so you don't need additional parenthesis
#order is exponents(**), multiplcation/ division, addition/subtraction
#HOWEVER we can add parenthesis to add that to the front of the order

x=10
x+=3
print(x)

y=10
y-=3
print(y)

print(10+3*2)

z=(2+3) * 10 -2
print(z)

#while // can round your division, you can also use a general funciton to round floaters in general
aa=2.9
print(round(aa))
#you can also print the absolute value of a number
print(abs(-123))
#search python 3 math module for more math documentation- like ceilings and floors

