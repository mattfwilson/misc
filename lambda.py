import functools

find_tip = lambda bill: bill * .06 + bill * .2
print(find_tip(125))

boomed_words = []

def boom(input):
    uppercase = input.upper()
    return boomed_words.append(uppercase)

boom("hello")
boom("lol")
boom('elden ring')
print(boomed_words)

lambda_upper = lambda input: input.upper()

names = ["mike", "att", "thry", "jonelle", "hptp", "jkjk", "hope", "qwerty", "awsd"]
no_vowels = filter(lambda name: name[0] == "a" or name == "jkjk" or name != "qwerty", names)
print(list(no_vowels))

lst = [8, 21, 5, -101, 4, 783, -51]
print(functools.reduce(lambda a, b: a if a <= b else b, lst))