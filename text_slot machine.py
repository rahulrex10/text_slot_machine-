import random  # Import the random module for generating random values

# Constants for the game
MAX_LINES = 3  # Maximum number of lines a player can bet on
MAX_BET = 100  # Maximum bet amount
MIN_BET = 1  # Minimum bet amount

# Dimensions of the slot machine
ROWS = 3  # Number of rows in the slot machine display
COLS = 3  # Number of columns in the slot machine display

# Symbol counts for the slot machine
symbol_count = {
    "cherry": 2,
    "bar": 4,
    "7": 6,
    "bell": 8
}

# Symbol values for calculating winnings
symbol_value = {
    "cherry": 5,
    "bar": 4,
    "7": 3,
    "bell": 2
}


# Function to check winnings on each line
def checking_winnings(columns, lines, bet, values):
    winnings = 0  # Initialize total winnings
    winning_lines = []  # List to store winning lines
    for line in range(lines):
        symbol = columns[0][line]  # Get the symbol in the current line
        for column in columns:
            symbol_to_check = column[line]  # Get the symbol to check in the current column
            if symbol != symbol_to_check:
                break  # If symbols don't match, exit the loop
        else:
            winnings += values[symbol] * bet  # Calculate winnings for the line
            winning_lines.append(line + 1)  # Append the winning line number
    return winnings, winning_lines  # Return total winnings and winning lines


# Function to simulate a spin of the slot machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # List to store all symbols based on their counts
    for symbol, SYMBOL_COUNT in symbols.items():
        for _ in range(SYMBOL_COUNT):
            all_symbols.append(symbol)

    columns = []  # List to store the slot machine display columns
    for _ in range(cols):
        column = []  # List to store symbols in a column
        current_symbols = all_symbols[:]  # Create a copy of all symbols
        for _ in range(rows):
            value = random.choice(current_symbols)  # Choose a random symbol
            current_symbols.remove(value)  # Remove the chosen symbol from the available symbols
            column.append(value)  # Add the chosen symbol to the column

        columns.append(column)  # Add the column to the slot machine display

    return columns  # Return the slot machine display


# Function to print the slot machine display
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print each symbol in a row with separators
            else:
                print(column[row], end="")  # Print the last symbol without a separator

        print()  # Move to the next line for the next row


# Function to handle player deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")  # Prompt user for deposit amount
        if amount.isdigit():  # Check if the input is a digit
            amount = int(amount)  # Convert amount to an integer
            if amount > 0:  # Check if the amount is greater than 0
                break  # If valid, break out of the loop
            else:
                print("Amount must be greater than 0.")  # Print an error message
        else:
            print("Please enter a number.")  # Print an error message for non-numeric input
    return amount  # Return the valid deposit amount


# Function to get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")  # Prompt user for lines
        if lines.isdigit():  # Check if the input is a digit
            lines = int(lines)  # Convert lines to an integer
            if 1 <= lines <= MAX_LINES:  # Check if lines are within valid range
                break  # If valid, break out of the loop
            else:
                print("Enter a valid number of lines.")  # Print an error message
        else:
            print("Please enter a number.")  # Print an error message for non-numeric input
    return lines  # Return the valid number of lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line ? $")  # Prompt user for bet amount
        if amount.isdigit():  # Check if the input is a digit
            amount = int(amount)  # Convert amount to an integer
            if MIN_BET <= amount <= MAX_BET:  # Check if bet amount is within valid range
                break  # If valid, break out of the loop
            else:
                print(f"Amount must be between ${MIN_BET} - {MAX_BET}.")  # Print an error message
        else:
            print("Please enter a number.")  # Print an error message for non-numeric input

    return amount  # Return the valid bet amount


def spin(balance):
    lines = get_number_of_lines()  # Get the number of lines from the user
    while True:
        bet = get_bet()  # Get the bet amount from the user
        total_bet = bet * lines  # Calculate the total bet amount

        if total_bet > balance:
         print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")  # Print an error msg
        else:
            break  # If valid, break out of the loop

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Spin the slot machine
    print_slot_machine(slots)  # Print the slot machine display

    winnings, winning_lines = checking_winnings(slots, lines, bet, symbol_value)  # Check winnings
    print(f"You won ${winnings}.")
    print(f"You won on lines", *winning_lines)
    return winnings - total_bet  # Return the net result of the spin


def main():
    balance = deposit()  # Get the initial balance from the user
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)  # Update the balance based on the result of the spin

    print(f"You are left with ${balance}")  # Print the final balance


if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
