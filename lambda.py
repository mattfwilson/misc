import reduce

find_tip = lambda bill: bill * .06 + bill * .2
print(find_tip(125))

def boom(input):
    uppercase = input.upper()
    return print(uppercase)

boom("hello")

lambda_upper = lambda input: input.upper()
print(lambda_upper)


names = ["mike", "att", "thry", "jonelle", "hptp", "jkjk", "hope", "qwerty", "awsd"]
no_vowels = filter(lambda name: name[0] == "a" or name == "jkjk" or name != "qwerty", names)
print(list(no_vowels))

reduced = reduce(lambda name: name)