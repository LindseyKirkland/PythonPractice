#defining if statements

the_weekend = False
the_week = False
wednesday = True

if the_weekend:
    print("yay! it's the weekend")
    print('enjoy')
elif the_week:
    print("it's still the week")
    print("hang in there")
elif wednesday:
    print("it is wednesday my dudes")
else:
    print("it's friday!")
    print("get ready for the weekend")

#down payment on a house exercise
# good_credit = False

# if good_credit:
#     print("down payemnt is", 1000000 *.1)
# else:
#     print("down payment is", 1000000 *.2)

#try number 2


# goodcredit = True

# price = 1000000

def cred_check (credit, price):
    if credit == 'good':
        downpayment =(price * .1)
    else:
        downpayment=(price * .2)
    print(f"Down payemnt is: ${downpayment }")


cred_check('bad', 15000)