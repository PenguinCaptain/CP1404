from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

MILES_KM_FACTOR = 1.60934


class ConvertMilesKmApp(App):
    """SquareNumberApp is a Kivy App for squaring a number"""

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def increment(self, value=1):
        """Increase the input number by the given value"""
        try:
            input_number = float(self.root.ids.input_number.text)
            self.root.ids.input_number.text = str(input_number + value)
        except ValueError:
            self.root.ids.input_number.text = str(float(value))

    def convert(self):
        """Convert the input miles to kilometers"""
        try:
            input_number = float(self.root.ids.input_number.text)
            result = input_number * MILES_KM_FACTOR
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0.0"


ConvertMilesKmApp().run()
