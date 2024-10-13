"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_income_report(incomes, cumulative_totals):
    """Print the income report with cumulative totals."""
    print("\nIncome Report\n-------------")
    for month, (income, total) in enumerate(zip(incomes, cumulative_totals), start=1):
        print(
            "Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(
                month, income, total
            )
        )


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    # Calculate cumulative totals
    cumulative_totals = []
    total = 0
    for income in incomes:
        total += income
        cumulative_totals.append(total)

    print_income_report(incomes, cumulative_totals)


main()
