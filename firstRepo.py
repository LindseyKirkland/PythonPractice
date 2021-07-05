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