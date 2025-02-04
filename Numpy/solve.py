
def input_output():
    name : str = input("Enter your name: ")
    age : int = input("enter your age: ")
    add : str = input("enter your address: ")

    print(f"Hi! {name}, \n your age is - {age} \n and you current address in : {add}")

def swap(a, b):
    a = a+b
    b = a-b
    a = a-b

    return a,b

def convert_float_to_int(a):
    
    return int(a)

def is_positive(a):

    return True if a >= 0 else False

def odd_even(a):

    return "Even" if a%2 == 0 else "ODD"

def is_vowel(char):

    vowels = "aeiou"

    return True if char in vowels else False

# a = -2
# print(is_vowel('i'))

# a = 10.43
# a = convert_float_to_int(a)
# print(type(a))


# a = 5
# b = 10

# a,b = swap(a, b)
# print(f"after swap : {a} , {b}")

# input_output()
