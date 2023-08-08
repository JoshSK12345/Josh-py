# In this programme, the user would like to convert a customer bill
# amount into words to be printed on a receipt issued at a
# supermarket teller.

# The program contains a python class called "DigitsToWords" and a method in the class called "numbers_to_words"

from numbers_to_words_OOP import DigitsToWords

customer_bill = 33457
# Supposing the above is the total customer bill to be paid at the counter.
# Applying the program begins with instantiating the class "DigitsToWords"

bill = DigitsToWords(customer_bill)

# An object of the class is created below, called "bill_in_words".
bill_in_words = bill.numbers_to_words()

# The print statement below shows that the customer bill, stated alongside its value/label in words.

print(f"Dear customer, your total bill is: {customer_bill} ({bill_in_words})")

# The program returns the output below:
# 

