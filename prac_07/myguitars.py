import csv

from guitar import Guitar

FILE = "guitars.csv"


def main():
    """Main function"""
    guitars = load_guitars()
    guitars.sort()
    print_guitars(guitars)


def print_guitars(guitars):
    """Print guitars."""
    longest_name_length = max(len(guitar.name) for guitar in guitars)
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_str = "(vintage)" if guitar.is_vintage() else ""
        name_str = f"{guitar.name:>{longest_name_length}}"
        cost_str = f"${guitar.cost:10,.2f}"
        print(f"Guitar {i}: {name_str} ({guitar.year}), worth {cost_str} {vintage_str}")


def load_guitars():
    """Load guitars from file."""
    with open(FILE, "r") as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        guitars = []
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars


if __name__ == "__main__":
    main()
