def total_bill(total, tip_n_tax):
    return total + tip_n_tax(total)

def tip_tax(bill):
    tip = bill * .20
    tax = bill * .06
    total = tip + tax
    return total

print(total_bill(100, tip_tax))