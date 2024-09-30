from score import judge

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    output = get_score()

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            output = get_score()
        elif choice == "P":
            print(output[0])
        elif choice == "S":
            print_star(output[1])

        print(MENU)
        choice = input(">>> ").upper()

    print("Good Bye.")


def get_score():
    score = int(input("Enter the score: "))
    result = judge(score)
    while result.startswith("Invalid"):
        score = int(input("Invalid number. Re-enter the score: "))
        result = judge(score)
    return result, score


def print_star(score):
    print("*" * int(score))


if __name__ == "__main__":
    main()
