import functools

boomed_words = []

def boom(input):
    uppercase = input.upper() + " has been boomed!"
    return boomed_words.append(uppercase)

boom("hello")
boom("lol")
boom('elden ring')
for boomers in boomed_words:
    print(boomers)
print(f"{len(boomed_words)} words have been boomed.")

lambda_upper = lambda input: input.upper()

names = ["mike", "att", "thry", "jonelle", "hptp", "jkjk", "hope", "qwerty", "awsd"]
no_vowels = filter(lambda name: name[0] == "a" or name == "jkjk" or name != "qwerty", names)
print(list(no_vowels))

lst = [8, 21, 5, -101, 4, 783, -51]
print(functools.reduce(lambda a, b: a if a <= b else b, lst))