num = 0
word = 'lol'
boolean = False

def changeVars(input1, input2, input3):
    input1 = 5
    input2 = 'haha'
    input3 = True
    return input1, input2, input3
    
print(num)
print(word)
print(boolean)

num, word, boolean = changeVars(num, word, boolean)

print(num)
print(word)
print(boolean)