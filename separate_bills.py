GRAND_TOTAL = 350
NAMES = ["Molly", "Matt", "Janelle", "Max", "Tim", "Colette", "Brian", "Amanda", "Shawn", "Katie", "Misc Person"]

def separate_checks(bill, people):
    def add_tax(bill, people):
        tax = bill * .06
        tax_total = bill + tax
        print(f"Total with tax is {tax_total}")
        return tax_total
    def add_tip():
        tip = bill * .2
        tip_total = bill * tip
        print(f"Total with tip is {tip_total}")
        return tip_total
    def split_total():
        num_people = len(people)
        split_totals = bill / num_people
        print(bill)
        return split_totals
    add_tax(bill, people)

separate_checks(GRAND_TOTAL, NAMES)

# def add_tax(total):
#     tax = total * .06
#     tax_total = total + tax
#     print(f"Total with tax is {tax_total}")
#     return tax_total

# def add_tip(total):
#     tip = total * .2
#     tip_total = total + tip
#     print(f"Total with tip is {tip_total}")
#     return tip_total

# def split_total(total, total_list):
#     num_people = len(total_list)
#     split_totals = total / num_people
#     print(total)
#     return split_totals

# def total_bills(tax_func, tip_func, dividing, bills, names):
#     split_bills = []
#     tip_and_tax = tax_func(bills) + tip_func(bills)
#     split_checks = round(dividing(tip_and_tax, names), 3)
#     for name in names:
#         split_bills.append(f"{name} owes {split_checks}!")
#     return split_bills

# # party_total = input(f'What is your total bill? ')

# TOTAL_PER_PERSON = total_bills(add_tax, add_tip, split_total, TOTAL_PER_PERSON, NAMES)
# for person in TOTAL_PER_PERSON:
#     print(person)