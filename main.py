from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
import random
import math


class BatmanApp(App):

    def build(self):
        self.sound = SoundLoader.load("dog.mp3")
        self.clicks = 0
        self.old_positions = []

        root = FloatLayout()

        # Home screen title
        title = Label(
            text="🐶 NEW BAKCHODI🦇",
            font_size=28,
            size_hint=(1, None),
            height=60,
            pos_hint={"center_x": 0.5, "top": 1}
        )
        root.add_widget(title)

        # Main button
        self.button = Button(
            text="STOP",
            size_hint=(None, None),
            size=(140, 55),
            font_size=20,
            halign="center",
            valign="middle",
            text_size=(130, 50),
            background_normal="",
            background_color=(1, 0, 0, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )

        self.button.bind(on_press=self.button_pressed)
        root.add_widget(self.button)

        # Sound automatically start
        if self.sound:
            self.sound.loop = True
            self.sound.play()

        return root

    def get_far_position(self):
        button = self.button

        max_x = max(0, int(Window.width - button.width))
        max_y = max(70, int(Window.height - button.height))

        old_x, old_y = button.pos

        # 100 baar tak door aur nayi jagah dhoondenge
        for _ in range(100):

            x = random.randint(0, max_x)
            y = random.randint(60, max_y)

            # Purani location se distance
            distance = math.sqrt(
                (x - old_x) ** 2 +
                (y - old_y) ** 2
            )

            # Har purani location se bhi door rahe
            far_from_old_locations = True

            for old_pos in self.old_positions:
                old_distance = math.sqrt(
                    (x - old_pos[0]) ** 2 +
                    (y - old_pos[1]) ** 2
                )

                if old_distance < 180:
                    far_from_old_locations = False
                    break

            # Current location se bhi kaafi door
            if distance > min(Window.width, Window.height) * 0.35:
                if far_from_old_locations:
                    return x, y

        # Agar suitable jagah na mile to random nayi jagah
        return (
            random.randint(0, max_x),
            random.randint(60, max_y)
        )

    def button_pressed(self, button):

        # Pehli 3 taps
        if self.clicks < 3:

            self.clicks += 1

            button.pos_hint = {}

            # Current position save
            self.old_positions.append(button.pos)

            # Bahut door nayi location
            new_x, new_y = self.get_far_position()

            button.pos = (new_x, new_y)

        # 4th tap
        elif self.clicks == 3:

            self.clicks += 1

            button.text = "BATMAN MERA PAPA HAI 😂"

            button.background_color = (0, 1, 0, 1)

            # Text button ke andar fix rahe
            button.font_size = 17
            button.text_size = (130, 50)

        # Green button ke baad
        else:

            if self.sound:
                self.sound.stop()

            button.disabled = True


BatmanApp().run()