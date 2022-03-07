bills = [100, 57, 133, 89, 218]

# def add_tax(total):
#     tax = total * .06
#     new_total = total + tax
#     return new_total

# def add_tip(total):
#     tip = total * .20
#     new_total = total + tip
#     return new_total

def double(num):
    return num * 2

doubled = map(double, bills)
print(doubled)
print(list(doubled))