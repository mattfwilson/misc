def title_decorator(print_name_func):
    def wrapper(*args):
        print(f"Hello,")
        print_name_func(*args)
    return wrapper

@title_decorator
def print_name(name):
    print(name)

print_name("Matt")
