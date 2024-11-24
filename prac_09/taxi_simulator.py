from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


class TaxiSimulator:
    taxi_list = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4),
    ]

    def __init__(self):
        """Initialise the TaxiSimulator"""
        self.current_taxi = None
        self.current_bill = 0

    def start(self):
        """Start the TaxiSimulator"""
        print("Let's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()
        while menu_choice != "q":
            if menu_choice == "c":
                self.choose_taxi()
            elif menu_choice == "d":
                self.drive_taxi()
            else:
                print("Invalid option")
            print(f"Bill to date: ${self.current_bill}")

            print("q)uit, c)hoose taxi, d)rive")
            menu_choice = input(">>> ").lower()
        print(f"Total trip cost: ${self.current_bill}")
        print("Taxis are now:")
        self.display_taxis()

    def display_taxis(self):
        """Display the taxis"""
        for i, taxi in enumerate(self.taxi_list):
            print(f"{i} - {taxi}")

    def choose_taxi(self):
        """Choose a taxi"""
        print("Taxis available:")
        self.display_taxis()
        try:
            taxi_choice = int(input("Choose taxi: "))
        except ValueError:
            print("Invalid input")
            return
        if taxi_choice < 0 or taxi_choice >= len(self.taxi_list):
            print("Invalid taxi choice")
            return

        self.current_taxi = self.taxi_list[taxi_choice]

    def drive_taxi(self):
        """Drive the taxi"""
        if self.current_taxi is None:
            print("You need to choose a taxi before you can drive")
            return
        try:
            distance = int(input("Drive how far? "))
        except ValueError:
            print("Invalid input")
            return
        if distance < 0:
            print("Invalid input")
            return
        self.current_taxi.start_fare()
        self.current_taxi.drive(distance)
        print(
            f"Your {self.current_taxi.name} trip cost you ${self.current_taxi.get_fare()}"
        )
        self.current_bill += self.current_taxi.get_fare()


if __name__ == "__main__":
    TaxiSimulator().start()
