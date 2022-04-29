tip_percent = 0
fed_tax = 0
state_tax = 0
total_bill = 0

total_bill = input('How much is your bill? ')
total_bill = int(total_bill)
tip_percent = input('How much tip in percent? ')
tip_percent = float(tip_percent)
fed_percent = input('How much is fed tax in percent? ')
fed_percent = float(fed_percent)
state_percent = input('How much is state tax in percent? ')
state_percent = float(state_percent)

def tip_tax(bill, tax, state, tip):
    taxed = bill * tax
    stated = bill * state
    tipped = bill * tip
    total = bill + taxed + stated + tipped
    print('Fed tax: $' + '{:.2f}'.format(taxed))
    print('State tax: $' + '{:.2f}'.format(stated))
    print('Tip: $' + '{:.2f}'.format(tipped))
    return print('The total amount owed is $' + '{:.2f}'.format(total))

result = tip_tax(total_bill, fed_percent, state_percent, tip_percent)