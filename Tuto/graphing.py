from manim import *

class Graphing(Scene):
    def construct(self):
        
        plane = NumberPlane(
            x_range = [-4,4,2], x_length = 7, y_range = [0,16,4], y_length = 5
        ).to_edge(DOWN).add_coordinates()
        labels = plane.get_axis_labels(x_label = 'x', y_label = "y") 
        parab = plane.plot(lambda x : x**2, x_range = [-4,4], color = GREEN)
        func_label = MathTex("y = x^2").scale(1.2).next_to(parab, RIGHT, buff = .3).set_color(BLUE)
        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(parab, labels, func_label)), run_time = 2.5)
        
        area = plane.get_riemann_rectangles(graph = parab, x_range = [-2,3], dx = .2, stroke_width = .1, stroke_color = WHITE)

        self.play(Create(area), run_time = 2)