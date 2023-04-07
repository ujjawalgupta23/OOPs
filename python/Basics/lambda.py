"""If you want to use a funciton only one time, so you use lambda function"""

double = lambda x: 2 * x
print(double(4))

add = lambda x, y: x + y
print(add(4, 6))

multiply = lambda x, y: x * y
print(multiply(5, 7))

full_name = lambda first_name, last_name: first_name + ' ' + last_name
print(full_name("Ujjawal", "Gupta"))

age_check = lambda age: True if age >= 18 else False
print(age_check(20))