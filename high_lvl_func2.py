tip = 0
tax = 0
bill = 0

bill = input('How much is your bill? ')
tip = input('How much do you want to tip? ')
tax = input('How much is tax? ')

print(type(tip))
print(type(tax))

def total_bill(total, tip_n_tax):
    return total + tip_n_tax(total)

def tip_tax(bill):
    tipped = bill * tip
    taxed = bill * tax
    total = tipped + taxed
    return total

result = total_bill(bill, tip_tax)