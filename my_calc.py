def sum(x, y):
    return x + y

def subt(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Can't divide by zero"

def sq(x, y):
    return x ** y