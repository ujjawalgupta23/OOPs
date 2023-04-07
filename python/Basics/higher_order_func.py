"""HIgher Order Function 1: Accepts a function as argument
                         2: returns a function"""

# 1st


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func, string):
    text = func(string)
    print(text)


hello(quiet, "ujjAwAl")
hello(loud, "uJJawaL")


# 2nd
def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(5)
print(divide(100))
