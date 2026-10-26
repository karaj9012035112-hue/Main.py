from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class CounterApp(App):

    def build(self):
        self.count = 0

        main_layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=20
        )

        self.counter_label = Label(
            text=str(self.count),
            font_size=50
        )

        button_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(1, None),
            height=80,
            spacing=10
        )

        self.count_button = Button(
            text="Count +1",
            font_size=22
        )

        self.reset_button = Button(
            text="Reset",
            font_size=22
        )

        self.count_button.bind(
            on_press=self.increase_count
        )

        self.reset_button.bind(
            on_press=self.reset_count
        )

        button_layout.add_widget(self.count_button)
        button_layout.add_widget(self.reset_button)

        main_layout.add_widget(self.counter_label)
        main_layout.add_widget(button_layout)

        return main_layout

    def increase_count(self, instance):
        self.count += 1
        self.counter_label.text = str(self.count)

    def reset_count(self, instance):
        self.count = 0
        self.counter_label.text = str(self.count)


if __name__ == "__main__":
    CounterApp().run()