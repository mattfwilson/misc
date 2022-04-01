def title_decorator(print_name_func):
    def wrapper(*args):
        print(f"Hello,")
        if args == "Janelle":
            print("lol")
        else:
            print_name_func(*args)
    return wrapper

def lol_decorator(lold):
    def wrapper(*args):
        if args == "Janelle":
            print("You are a lol")
        else:
            lold(*args)
    return wrapper

@lol_decorator
def print_name(name, age, hobby):
    print(F"{name} you are {age} years old who is interested in {hobby}!")

print_name("Janelle", 35, "sports")
