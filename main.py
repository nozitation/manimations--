from manim import *

class LaTex(Scene):
    def construct(self):
        lt = Tex(r"\LaTeX", font_size=144)
        self.play(Write(lt))
class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.play(Write(equation))
class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.play(Write(equation))
class fourier_transform_formula(Scene):
    def construct(self):
        ft = MathTex(r"f(w) = \int_{-\infty}^{\infty} f(t)e^{-i2\pi wt}dt")
        self.play(Write(ft))