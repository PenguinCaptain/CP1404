class Project:
    """Represents a project object"""

    def __init__(
        self, name, start_date, priority=0, estimated_cost=0, completion_percentage=0
    ):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = estimated_cost
        self.completion_percentage = completion_percentage

    def is_started(self, current_date):
        """Determine if the project has started."""
        return self.start_date <= current_date

    def __str__(self):
        """Return a string representation of a Project."""
        return f"{self.name}, \
start: {self.start_date.strftime('%d/%m/%Y')}, \
priority: {self.priority}, \
estimate: ${self.cost_estimate:.2f}, \
percentage: {self.completion_percentage:.0f}%"

    def __lt__(self, other):
        """Less than comparison for Project objects."""
        return self.priority < other.priority
