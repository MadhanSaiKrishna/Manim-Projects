from manim import *

class createCircle(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(PINK, opacity=0.5)
		self.play(Create(circle));

class SquareToCircle(Scene):
	def construct(self):
		circle = Circle()
		circle.set_fill(PINK,opacity = 0.75)

		square = Square()
		square.set_fill(BLUE,opacity = 0.5)
		square.rotate(PI/4)


		self.play(Create(square))
		self.play(Transform(square,circle))
		self.play(FadeOut(square))