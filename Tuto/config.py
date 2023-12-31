from manim import *


class config(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=5,
            y_length=5,
            axis_config={
                "include_numbers": True,
                "font_size":30,
                "include_tip":True,
                "numbers_to_exclude":[0],
                "numbers_with_elongated_ticks":[0,2],
            },
        )

        self.add(ax)
        self.wait()
