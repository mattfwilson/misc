bills = [100, 57, 133, 89, 218]
new_bills = []
names = ["Molly", "Matt", "Janelle", "Max", "Tim", "Colette", "Brian", "Amanda", "Shawn", "Katie"]

def add_tax(total):
    tax = total * .06
    new_total = total + tax
    return new_total

def add_tip(total):
    tip = total * .20
    new_total = total + tip
    return new_total

for i in range(len(bills)):
  total = add_tip(bills[i])
  new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you!")

for x in new_bills:
    print(x)

for name in range(len(names)):
    print(name)

# doubled = map(lambda bill: bill * 2, bills)
# print(doubled)
# print(list(doubled))