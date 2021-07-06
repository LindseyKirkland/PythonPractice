#using the AND operator
#If we have multiple Booleans defined as True, we can write an and statement

is_slimy = True
has_Shell = False

if is_slimy and has_Shell:
    print("it's a snail")

if is_slimy:
    print("it's a slug")

if is_slimy or has_Shell:
    print("it's a mollusk")
else: print("it's another animal")

#in addition to 'and' and 'or', you can also use 'not' as a boolean value
#use "and" to connect the statements and "not" to print the statement if it's false.
writing_tool = True
has_graphite = False

if writing_tool and not has_graphite:
    print("it's a pen")
if writing_tool and has_graphite:
    print("it's a pencil")

#comparison operators
# >(greater than), <(less than), >=(greater than or equal to), <=(less than or equal to), ==(equal to)
#(!=), not equal to

#Password check
password_characters = 10
if password_characters < 10:
    print("Password needs at least 10 characters")
elif password_characters > 50:
    print("Password cannot exceed 50 characters")
else:
    print("Password looks great!")

#len() returns the number of objects in a string

pattern_types = ('stripes', 'floral', 'polka dots')
pattern_types2 = ("stripes and floral and polka dots")
print(len(pattern_types))
print(len(pattern_types2))