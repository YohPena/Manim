from manim import *

class Getters(Scene):
    def construct(self):
        
        rect = Rectangle(color = WHITE, fill_color = BLUE, fill_opacity = .4, width = 2.5, height = 3).to_edge(UL)
        circ = Circle().to_edge(DOWN)
        arrow = always_redraw(
            lambda : Line(
                start = rect.get_bottom(), end = circ.get_top(), buff = .2
            ).add_tip()
        )

        
        self.play(Create(VGroup(rect, circ, arrow)), run_time = 3)
        self.play(rect.animate.to_edge(UR), circ.animate.scale(2))

class Updaters(Scene):
    def construct(self):
        nb = MathTex("ln(2)")
        box = always_redraw(
            lambda : SurroundingRectangle(
                nb, color = RED, fill_color = BLUE, fill_opacity = .4, buff = 1
            ))
        name = always_redraw(
            lambda : Tex("Yohan").next_to(box, DOWN, buff = 1)
        ) 

        self.play(Create(VGroup(nb, box, name)), run_time = 2)
        self.play(nb.animate.shift(RIGHT*2), run_time = 2)