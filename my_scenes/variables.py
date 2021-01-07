#!/usr/bin/env python
from manim import *

# To watch one of these scenes, run the following:
# python --quality m manim example_scenes.py SquareToCircle -p
#
# Use the flag --quality l for a faster rendering at a lower quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have preview of the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)


class OpeningManimExample(Scene):
    def construct(self):
        square = Square()
        self.play(ShowCreation(square))


class Variable(VGroup):
    def __init__(self, name='', content=None):
        self.super().__init__()
        self.name = name
        self.content = content
        self.variable_container = Square()
