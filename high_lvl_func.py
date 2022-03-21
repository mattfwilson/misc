from functools import reduce

bills = [100, 57, 133, 89, 218]
names = ["Molly", "Matt", "Janelle", "Max", "Tim", "Colette", "Brian", "Amanda", "Shawn", "Katie", "Misc"]

def add_tax(total):
    tax = total * 4
    new_total = total + tax
    return new_total

def add_tip(total):
    tip = total * 2
    new_total = total + tip
    return new_total

def divide_by_list(total, total_list):
    amount_of_people = len(total_list)
    separate_totals = 100 / amount_of_people
    return separate_totals

def total_bills(tax_func, tip_func, dividing, bills, names):
    new_bills = []
    tip_and_tax = tax_func(bills) + tip_func(bills)
    divided = round(dividing(tip_and_tax, names), 2)
    for i in names:
        print(f"{i} owes {divided}!")
    return new_bills

owed_by_person = total_bills(add_tax, add_tip, divide_by_list, bills, names)
print(owed_by_person)

# a_in_name = filter(lambda name: "a" not in name and "l" in name, names)
# a_names = list(a_in_name)
# print(a_names)

# reduced_ints = reduce(lambda x,y: x+y, bills)
# print(reduced_ints)

# tipped_bill = total_bills(add_tip, add_tax, bills)
# for item in tipped_bill:
#     print(item)


# doubled = map(lambda bill: bill * 2, bills)
# print(doubled)
# print(list(doubled))