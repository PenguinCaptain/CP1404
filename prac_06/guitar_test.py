from prac_06.guitar import Guitar


def test():
    """Test the Guitar class."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013)
    test_guitar(guitar1, "get_age", 102)
    test_guitar(guitar2, "get_age", 11)
    test_guitar(guitar1, "is_vintage", True)
    test_guitar(guitar2, "is_vintage", False)


def test_guitar(guitar, test_method, expected_value):
    """Test a guitar method and print the result."""
    actual_value = getattr(guitar, test_method)()
    print(
        f"{guitar.name} {test_method}() - Expected {expected_value}. Got {actual_value}"
    )


if __name__ == "__main__":
    test()
