from prac_06.guitar import Guitar


def main():
    """main function to run the program"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    longest_name_length = 0
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $").replace(",", ""))
        longest_name_length = max(longest_name_length, len(name))
        try:
            guitar = Guitar(name, year, cost)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_str = "(vintage)" if guitar.is_vintage() else ""
        name_str = f"{guitar.name:>{longest_name_length}}"
        cost_str = f"${guitar.cost:10,.2f}"
        print(f"Guitar {i}: {name_str} ({guitar.year}), worth {cost_str} {vintage_str}")


if __name__ == "__main__":
    main()
