from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["John", "Paul", "George", "Ringo"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            self.create_label(name)
        return self.root

    def create_label(self, label_text):
        """Create a label widget and add it to the GUI"""
        label_widget = self.create_label_widgets(label_text)
        self.root.ids.main.add_widget(label_widget)

    def create_label_widgets(self, label_text):
        """Create a widget that contains a label and a delete button"""
        label_layout = BoxLayout(orientation="horizontal", size_hint_y=0.2)
        label = Label(text=label_text, font_size=48)

        label_layout.add_widget(label)

        delete_button = Button(text="Delete", size_hint_x=0.1)
        # bind the button to the delete function
        delete_button.bind(on_press=self.handle_delete)
        label_layout.add_widget(delete_button)
        return label_layout

    def handle_delete(self, instance):
        """Remove the label layout when the delete button is pressed"""
        main_layout = self.root.ids.main
        label_layout = instance.parent
        main_layout.remove_widget(label_layout)


DynamicLabelsApp().run()
