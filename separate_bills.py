from functools import reduce

TOTAL_PER_PERSON = 150
NAMES = ["Molly", "Matt", "Janelle", "Max", "Tim", "Colette", "Brian", "Amanda", "Shawn", "Katie", "Misc Person"]

def add_tax(total):
    tax = total * .4
    new_total = total + tax
    return new_total

def add_tip(total):
    tip = total * .2
    new_total = total + tip
    return new_total

def split_total(total, total_list):
    amount_of_people = len(total_list)
    separate_totals = total / amount_of_people
    return separate_totals

def total_bills(tax_func, tip_func, dividing, bills, names):
    new_bills = []
    tip_and_tax = tax_func(bills) + tip_func(bills)
    divided = round(dividing(tip_and_tax, names), 3)
    for i in names:
        new_bills.append(f"{i} owes {divided}!")
    return new_bills

# party_total = input(f'What is your total bill? ')

TOTAL_PER_PERSON = total_bills(add_tax, add_tip, split_total, TOTAL_PER_PERSON, NAMES)
print(TOTAL_PER_PERSON)