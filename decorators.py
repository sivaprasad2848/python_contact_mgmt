# decorator enna function create cheyyunnu
# func enna parameter original function-ne accept cheyyum
def decorator(func):

    # wrapper enna inner function create cheyyunnu
    def wrapper():

        # Original function execute aakunnathinu munne print cheyyum
        print("Before function")

        # Original function call cheyyunnu
        func()

        # Original function execute aayathinu shesham print cheyyum
        print("After function")

    # wrapper function return cheyyunnu
    return wrapper


# @decorator use cheyyumbol hello function decorator-il pass aakum
# Internally: hello = decorator(hello)
@decorator
def hello():

    # Original hello function
    print("Hello World")


# Decorator apply cheytha hello function call cheyyunnu
hello()