FILENAME = "wimbledon.csv"


def read_data():
    """Reads the data from the csv file"""
    entries = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        # Skip the header
        next(in_file)
        for line in in_file:
            entries.append(line.strip().split(","))

    return entries


def process_data(entries):
    """Processes the data and returns the results"""
    champion_wins = {}
    winning_country = set()
    for entry in entries:
        _, country, champion, *_ = entry
        champion_wins[champion] = champion_wins.get(champion, 0) + 1
        winning_country.add(country)

    return champion_wins, winning_country


def print_results(champion_wins, winning_country):
    """Prints the results"""
    print("Wimbledon Champions: ")
    for champion, wins in champion_wins.items():
        print(f"{champion} {wins}")

    print(f"\nThese {len(winning_country)} countries have won Wimbledon:")
    print(", ".join(sorted(winning_country)))


def main():
    print_results(*process_data(read_data()))


if __name__ == "__main__":
    main()
