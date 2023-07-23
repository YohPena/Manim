from manim import *

# Folders from where to get images. They are in the folder of the script SVGs.py so I
# can just put the name of the folder. If not, put the full path like "C:\Documents\Manim\etc"
HOME1 = "Images"
HOME2 = "SVG_Images"


class SVGs(Scene):
    def construct(self):
        icon = SVGMobject(
            f"{HOME2}\\Eminem_logo.svg"
        )  # from https://commons.wikimedia.org/wiki/File:Eminem_logo.svg
        im = ImageMobject(f"{HOME1}\\YP.jpg").scale(3)  # from somewhere fuck you take your's

        self.play(DrawBorderThenFill(icon))  # don't work with .png or .jpg

        self.play(FadeIn(im))
