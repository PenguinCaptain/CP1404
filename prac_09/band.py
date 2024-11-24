class Band:
    """Band class with musician collection."""

    def __init__(self, name):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musician_members = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join([str(member) for member in self.musician_members])})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, member):
        """Add a musician to the band."""
        self.musician_members.append(member)

    def play(self):
        """Return a string showing all musicians playing their first (or no) instrument."""
        return "\n".join([member.play() for member in self.musician_members])
