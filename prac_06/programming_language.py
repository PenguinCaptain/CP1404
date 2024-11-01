class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        name = self.name
        typing = self.typing
        reflection = self.reflection
        year = self.year
        return f"{name}, {typing} Typing, Reflection={reflection}, First appeared in {year}"
        # Python, Dynamic Typing, Reflection=True, First appeared in 1991
