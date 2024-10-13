MIN_LENGTH = 6


def main():
    password = get_password(MIN_LENGTH)
    print_password(password)


def get_password(min_length):
    password = input(f"Enter password ({min_length} characters minimum): ")
    while len(password) < min_length:
        password = input(
            f"Password too short! Re-enter password ({min_length} characters minimum): "
        )
    return password


def print_password(password):
    print("*" * len(password))


main()
