import random

# Constants
MIN_NUMBER = 1  # Minimum number in the range
MAX_NUMBER = 45  # Maximum number in the range
NUMBERS_PER_PICK = 6  # Number of numbers per quick pick


def generate_unique_numbers():
    """
    Generates a list of unique random numbers between MIN_NUMBER and MAX_NUMBER.
    """
    unique_numbers = set()

    while len(unique_numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        unique_numbers.add(number)

    return sorted(unique_numbers)


def format_quick_pick(numbers):
    """
    Formats a list of numbers into a string with uniform spacing.
    """
    return " ".join(f"{num:2}" for num in numbers)


def main():
    try:
        # Prompt user for the number of quick picks
        num_quick_picks = int(input("How many quick picks? "))
        if num_quick_picks <= 0:
            print("Please enter a positive integer for the number of quick picks.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    for _ in range(num_quick_picks):
        quick_pick = generate_unique_numbers()
        formatted_pick = format_quick_pick(quick_pick)
        print(formatted_pick)


if __name__ == "__main__":
    main()
