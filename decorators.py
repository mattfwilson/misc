def title_decorator(print_name_func):
    def wrapper(*args):
        print(f"Hello,")
        print_name_func(*args)
    return wrapper

@title_decorator
def print_name(name, age, hobby):
    print(F"{name} you are {age} years old who is interested in {hobby}!")

print_name("Janelle", 35, "sports")
