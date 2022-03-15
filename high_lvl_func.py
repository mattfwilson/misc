from functools import reduce

bills = [100, 57, 133, 89, 218]
names = ["Molly", "Matt", "Janelle", "Max", "Tim", "Colette", "Brian", "Amanda", "Shawn", "Katie"]

def add_tax(total):
    tax = total * .06
    new_total = total + tax
    return new_total

def add_tip(total):
    tip = total * .20
    new_total = total + tip
    return new_total

def divide_by_four(total):
    new_total = total / 4
    return new_total

def total_bills(func1, func2, func3, list, list2):
    new_bills = []
    for i in range(len(list)):
        tip_and_tax = func1(list[i]) + func2(list[i])
        divided = func3(tip_and_tax) / 4
    for x in list2:
        new_bills.append(f"Total amount {x} owes is $" + "{:.2f}".format(divided))
    return new_bills

name_plus_owed = total_bills(add_tax, add_tip, divide_by_four, bills, names)
print(name_plus_owed)

a_in_name = filter(lambda name: "a" not in name and "l" in name, names)
a_names = list(a_in_name)
print(a_names)

reduced_ints = reduce(lambda x,y: x+y, bills)
print(reduced_ints)

# tipped_bill = total_bills(add_tip, add_tax, bills)
# for item in tipped_bill:
#     print(item)


# doubled = map(lambda bill: bill * 2, bills)
# print(doubled)
# print(list(doubled))