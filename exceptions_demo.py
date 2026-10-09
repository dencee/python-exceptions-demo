def zero_division(num1=10, num2=0):
    quotient = num1 / num2
    return quotient

def value_error(str="not a number"):
    converted_num = int(str)
    return converted_num

def type_error():
    greeting = "meowdy purrtners"
    greeting += 42
    return greeting

def index_error():
    my_list = [1, 2, 3]
    last_num = my_list[10]
    return last_num

EXAMPLES = [
    zero_division,
    value_error,
    type_error,
    index_error,
]

def demo_exceptions():
    print("\n=== 1. Built-in exceptions ===")
    for demo_function in EXAMPLES:
        try:
            print("Before calling demo_function")
            demo_function()
            print("After calling demo_function")
        except:
            print("An exception occurred")

