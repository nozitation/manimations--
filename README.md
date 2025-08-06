This is a repo that holds all of the things I make in manim

# Fourier Transform

```python
  from manim import *
class fourier_transform_formula(Scene):
    def construct(self):
        ft = MathTex(r"\mathcal{F}(w) = \int_{-\infty}^{\infty} f(t)e^{-i2\pi wt}dt")
        self.play(Write(ft))
 ```

<video width="320" height="240" controls>
  <source src="file:\\C:\Users\recic\Desktop\Noahs_stuff\manimations\media\videos\fourier_transform\1080p60\fourier_transform_formula.mp4" type="video/mp4">
</video>