"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(",")  # Separate the data into its parts
        parts[2] = int(
            parts[2]
        )  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
    input_file.close()
    return data


def display_subject(data):
    """Display subject details"""
    for subject in data:
        print(
            "{} is taught by {:<12} and has {:>3} students".format(
                subject[0], subject[1], subject[2]
            )
        )


main()
