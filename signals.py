from manim import *

class DC(Scene):
	def construct(self):
		axes = Axes(x_range = [0 ,5, 1], y_range=[0, 5, 1], tips = True, axis_config = {"color" : GREEN}, x_length = 4, y_length = 4)
		axes.to_corner(UL)
		dc_signal = Line(axes.c2p(0,1), axes.c2p(5,1), color = BLUE)
		self.play(Create(axes),run_time = 2)
		self.wait(1)
		self.play(dc_signal.animate, rate_func = smooth, run_time = 4)
		self.wait(1)


class Step(Scene):
	def construct(self):
		axes = Axes(axis_config = {"color" : BLUE})
		self.play(Create(axes))

class Pulse(Scene):
	def construct(self):
		axes = Axes(axis_config = {"color" : RED})
