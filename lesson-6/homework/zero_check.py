def check(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Denominator can't be zero"
    return wrapper

@check
def div(a, b):
   return a / b
print(div(1, 0))
