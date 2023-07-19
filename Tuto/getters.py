from manim import *

class Getters(Scene):
    def construct(self):
        
        rect = Rectangle(color = WHITE, fill_color = BLUE, fill_opacity = .4, width = 2.5, height = 3).to_edge(UL)
        circ = Circle().to_edge(DOWN)
        arrow = Line(start = rect.get_bottom(), end = circ.get_top(), buff = .2).add_tip()
        
        self.play(Create(VGroup(rect, circ, arrow)), run_time = 3)
        self.play(rect.animate.to_edge(UR))