from manim import *

class Test(Scene):
    def construct(self):
        circ=Crcle(radius=2.4, color=WHITE)
        self.play(Create(circ))