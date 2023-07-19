from manim import *

class CreateThenFill(Scene):
    def construct(self):
        sq = Square(side_length = 1.5, stroke_color = BLUE) #create sq
        self.play(Create(sq), run_time=2) #display sq
        self.play(sq.animate.set_fill(GREEN, opacity = .75), run_time = 1) #fill sq

class CreateFilled(Scene):
    def construct(self):
        sq = Square(side_length = 1.5, stroke_color = BLUE, fill_color = GREEN, fill_opacity = .25) #create sq
        self.play(Create(sq),run_time = 3) #display sq already filled

#circ = Create(Circle())
#self.play(circ)
#Works but dirty