import time

def delay(function):
    def wrapper():
        time.sleep(2)
        function()
    return wrapper

@delay
def say_hello():
    print("Hello")

say_hello()