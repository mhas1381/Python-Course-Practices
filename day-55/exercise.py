class User:
    def __init__(self , name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args , **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_authenticated
def create_new_post(user):
    print(f"This is {user.name} new post in blog")

user1 = User("Mamad")
# create_new_post(user1)


def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        print(f"It returned {result}")
    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)

result = a_function(2,4,5)
