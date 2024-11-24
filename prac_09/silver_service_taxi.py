from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness"""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Get the price for the taxi trip"""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
