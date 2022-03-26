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