import kivy
import meep
import webcolors
kivy.require('1.9.0')

from kivy.app import App
from kivy.graphics import Color
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget


class MoopWidget(Widget):
    mo = ObjectProperty(meep.random_moop())
    color = ObjectProperty((1.0, 1.0, 1.0))

    def update_color(self):
        self.color = webcolors.hex_to_rgb_float(self.mo.express())
        with self.canvas:
            Color(*self.color)


class MoopMaleWidget(MoopWidget):

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.mo = meep.random_moop()

    def on_mo(self, instance, value):
        self.update_color()


class MoopWorld(Widget):
    pass


class MoopApp(App):
    def build(self):
        return MoopWorld()

if __name__ == '__main__':
    MoopApp().run()
