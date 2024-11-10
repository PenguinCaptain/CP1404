from prac_06.programming_language import ProgrammingLanguage


def main():
    """main function to run the program"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    print(python)

    lang_list = [
        ProgrammingLanguage("Java", "Static", True, 1995),
        ProgrammingLanguage("C++", "Static", False, 1983),
        python,
        ProgrammingLanguage("Visual Basic", "Static", False, 1991),
        ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
    ]
    print("The dynamically typed languages are:")
    for lang in lang_list:
        if lang.is_dynamic():
            print(lang.name)


if __name__ == "__main__":
    main()
