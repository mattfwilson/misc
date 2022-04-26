tip = .20
tax = .06
state_tax = .03
bill = 0

bill = input('How much is your bill? ')
bill = int(bill)

def total_bill(total):
    return ("The total amount owed is $" + "{:.2f}".format(total))

def tip_tax(bill, tax, state, tip):
    taxed = bill * tax
    stated = taxed * state
    total = stated * tip
    return total

def state_tax(bill):
    state = bill * .04
    state_total = state + bill
    return state_total

result = total_bill(bill)
print(result)