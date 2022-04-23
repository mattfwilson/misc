tip = 0
tax = 0
bill = 0

bill = input('How much is your bill? ')
bill = int(bill)

def total_bill(total, tip_n_tax):
    return ("The total amount owed is $" + "{:.2f}".format(total + tip_n_tax(total)))

def tip_tax(bill):
    gratuity = bill * .20
    taxed = bill * .06
    total = gratuity + taxed
    return total

result = total_bill(bill, tip_tax)
print(result)