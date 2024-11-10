"""
Project Management System
Time Estimation: 1 hour
"""

import csv
from datetime import datetime

from project import Project


def main():
    """Main function."""
    print("Welcome to the Project Management System")
    projects = load_projects()
    projects.sort()
    print_menu()
    choice = input(">>> ").upper()
    while choice and choice != "Q":
        if choice == "L":
            filename = validated_input("File name: ", default=DEFAULT_FILE)
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects")
        elif choice == "S":
            filename = validated_input("File name: ", default=DEFAULT_FILE)
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print_menu()
        choice = input(">>> ").upper()
    do_save = input(f"Would you like to save to {DEFAULT_FILE}? ")
    if do_save.lower().startswith("y"):
        save_projects(projects)
    print("Thank you for using project management software.")


def print_menu():
    """Print the menu."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def display_projects(projects):
    """Display all projects."""
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage < 1:
            print(project)
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage >= 1:
            print(project)


def filter_projects(projects):
    """Filter projects by date."""
    date = validated_input(
        "Show projects that start after date (dd/mm/YYYY): ",
        lambda x: datetime.strptime(x, "%d/%m/%Y"),
    )
    projects_by_date = sorted(projects, key=lambda project: project.start_date)
    for project in projects_by_date:
        if not project.is_started(date):
            print(project)


def add_project(projects):
    """Add a new project."""
    print("Let's add a new project")
    name = validated_input("Name: ")
    start_date = validated_input(
        "Start date (dd/mm/YYYY): ", lambda x: datetime.strptime(x, "%d/%m/%Y")
    )
    priority = validated_input("Priority: ", int, 0)
    cost_estimate = validated_input("Estimated cost: ", float)
    completion_percentage = validated_input("Completion percentage: ", float, 0)
    projects.append(
        Project(name, start_date, priority, cost_estimate, completion_percentage)
    )
    projects.sort()


def update_project(projects):
    """Update a project."""
    for i, project_to_update in enumerate(projects, 0):
        print(f"{i}: {project_to_update}")
    project_to_update = validated_input("Project choice: ", lambda x: projects[int(x)])
    print(project_to_update)
    project_to_update.completion_percentage = validated_input(
        "New Percentage: ", float, project_to_update.completion_percentage
    )
    project_to_update.priority = validated_input(
        "New Priority: ", int, project_to_update.priority
    )
    projects.sort()


def validated_input(prompt, converter=str, default=None):
    """Get validated input."""
    while True:
        try:
            input_str = input(prompt)
            if not input_str:
                if default is not None:
                    return default
                print("Input cannot be empty")
                continue
            return converter(input_str)
        except:  # noqa: E722 pylint: disable=bare-except
            print("Invalid input")


DEFAULT_FILE = "projects.txt"


def load_projects(filename=DEFAULT_FILE):
    """Load projects from a file."""
    with open(filename, "r", encoding="utf-8") as in_file:
        projects = []
        in_file.readline()
        reader = csv.reader(in_file, delimiter="\t")
        for row in reader:
            name, start_date, priority, estimated_cost, completion_percentage = row
            projects.append(
                Project(
                    name,
                    datetime.strptime(start_date, "%d/%m/%Y"),
                    int(priority),
                    float(estimated_cost),
                    float(completion_percentage),
                )
            )
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def save_projects(projects, filename=DEFAULT_FILE):
    """Save projects to a file."""
    with open(filename, "w", encoding="utf-8") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(
            [
                "Name",
                "Start Date",
                "Priority",
                "Estimated Cost",
                "Completion Percentage",
            ]
        )
        writer.writerows(
            [
                [
                    project.name,
                    project.start_date.strftime("%d/%m/%Y"),
                    project.priority,
                    project.cost_estimate,
                    project.completion_percentage,
                ]
                for project in projects
            ]
        )
    print(f"Saved {len(projects)} projects to {filename}")


if __name__ == "__main__":
    main()
