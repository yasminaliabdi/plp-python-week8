import random

def calculator():
    """Tool 1: Performs basic math operations."""
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op == "+":
            print(f"Result: {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1 * num2}")
        elif op == "/":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator.")
    except ValueError:
        print("Please enter valid numbers.")

def todo_list():
    """Tool 2: Manages a list of tasks that changes while running."""
    print("\n--- To-Do List ---")
    tasks = []
    
    while True:
        action = input("Type 'add', 'show', 'remove', or 'back': ").lower()
        
        if action == "add":
            item = input("Enter task: ")
            tasks.append(item)
            print(f"'{item}' added!")
        elif action == "show":
            if not tasks:
                print("Your list is empty.")
            else:
                print("Your Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif action == "remove":
            item = input("Enter task to remove: ")
            if item in tasks:
                tasks.remove(item)
                print(f"'{item}' removed.")
            else:
                print("Task not found.")
        elif action == "back":
            break
        else:
            print("Invalid action.")

def guessing_game():
    """Tool 3: A game using a loop and conditionals."""
    print("\n--- Number Guessing Game ---")
    secret = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            
            if guess < secret:
                print("Too low! Try again.")
            elif guess > secret:
                print("Too high! Try again.")
            else:
                print(f"Correct! You got it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# --- Part B: Build the Menu Loop ---

print("Welcome to Yasmin's Mini-Toolkit!")

while True:
    print("\n--- My Mini Toolkit ---")
    print("1. Simple Calculator")
    print("2. To-Do List")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        calculator()
    elif choice == "2":
        todo_list()
    elif choice == "3":
        guessing_game()
    elif choice == "4":
        print("Goodbye! Thanks for using the toolkit.")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")