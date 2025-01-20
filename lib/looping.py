# looping.py

# Function to print countdown from 10 to 1 and then "Happy New Year!"
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")

# Function to square integers in a given list
def square_integers(int_list):
    return [x ** 2 for x in int_list]

# Function for FizzBuzz from 1 to 100
def fizzbuzz():
    for i in range(1, 101):  # Loop through numbers from 1 to 100
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
