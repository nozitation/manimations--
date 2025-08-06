from manim import *
class fourier_transform_formula(Scene):
    def construct(self):
        ft = MathTex(r"\mathcal{F}(w) = \int_{-\infty}^{\infty} f(t)e^{-i2\pi wt}dt")
        self.play(Write(ft))