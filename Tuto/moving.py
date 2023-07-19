from manim import *

class MovingObject(Scene):
    def construct(self):

        name = Tex("Yohan").to_edge(UL, buff = .5) #create text, UL for Up Left
        sq = Square(side_length = 0.5).shift(LEFT, UP) #create square
        tri = Triangle().scale(.6) #create triangle
        self.play(Write(name), run_time = 3) #display the text (works with Create)
        self.play(Create(sq), run_time=2) #display the text (works with Write)
        self.play(Create(tri)) #display tri

        self.play(name.animate.to_edge(UR), run_time = 2) #move text 
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL).rotate(PI/3), run_time = 3) #animate simultaneously