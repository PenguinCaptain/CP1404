import random


def main():
    score = float(input("Enter score: "))
    print(judge(score))
    print(judge(random.randint(0, 100)))


def judge(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()
