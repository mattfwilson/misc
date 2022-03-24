find_tip = lambda bill: bill * .06 + bill * .2
print(find_tip(125))
def boom(input):
    uppercase = input.upper()
    return print(uppercase)

boom("hello")

lambda_upper = lambda input: input.upper()
print(lambda_upper)


names = ["mike", "att", "thry", "janelle", "hptp", "jkjk", "orly", "qwerty", "awsd"]
no_vowels = filter(lambda name: name[0] == "a" or name[0] == "e" or name[0] == "i" or name[0] == "o" or name[0] == "u", names)
print(list(no_vowels))