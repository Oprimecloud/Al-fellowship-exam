# # # defined fucntion for calculator
# # # question 1
def add(a, b):
    return(a + b)

def sub(a, b):
    return(a - b)

def multiply(a, b):
     return(a * b)

def divide(a, b):
    if b != 0:
        return(a / b)
    return("Division by zero error")
while True:
    print("=========welcome to basic calculator=====")
    print("Select operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", sub(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
    if choice == '5':
            print("Exiting the calculator.. Goodbye!")
            break






# quetion 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break    # break out of loop
    num = int(user_input)   # convert to integer
    if num % 2 == 0:
        print("The number is even")
        print("The number is odd")





# Quetion 3
while True:
    print()
    age = input("Enter your age (or type exit to quit): ")
    if age.title() == exit:
        print("Goodbye!")
        break
    try:
        age = int(age)
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except ValueError:
        print("Invalid input")

