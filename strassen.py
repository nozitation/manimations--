from manim import *

class strassen(Scene):
    def construct(self):
        title = Title(f"Strassen's algorithm")
        matrices = MathTex(
            r"\begin{bmatrix} A_1 & A_2 \\ A_3 & A_4 \end{bmatrix} \times \begin{bmatrix} B_1 & B_2 \\ B_3 & B_4 \end{bmatrix} = \begin{bmatrix} C_1 & C_2 \\ C_3 & C_4 \end{bmatrix}"
        ).shift(UP*2)
        M = VGroup(
            MathTex(r"(A_1 + A_4) \times (B_1 + B_4) = M_1", font_size=45),
            MathTex(r"        (A_3 + A_4) \times B_1 = M_2", font_size=45),
            MathTex(r"        A_1 \times (B_2 - B_4) = M_3", font_size=45), 
            MathTex(r"        A_4 \times (B_3 - B_1) = M_4", font_size=45), 
            MathTex(r"        (A_1 + A_2) \times B_4 = M_5", font_size=45), 
            MathTex(r"(A_3 - A_1) \times (B_1 + B_2) = M_6", font_size=45),
            MathTex(r"(A_2 - A_4) \times (B_1 + B_2) = M_7", font_size=45)
        ).next_to(matrices, DOWN*2).shift(LEFT*2)
        M[0][33:35].set_color(PURPLE)
        C = VGroup(
            MathTex(r"M_1 + M_4 - M_5 + M_7 = C_1", font_size=45), 
            MathTex(r"            M_3 + M_5 = C_2", font_size=45), 
            MathTex(r"            M_2 + M_4 = C_3", font_size=45), 
            MathTex(r"M_1 - M_2 + M_3 + M_6 = C_4", font_size=45)
        )
        self.add(title)
        self.play(Write(matrices), run_time=3)
        self.play(Write(M[0], reverse=True), Write(M[1].next_to(M[0], DOWN).shift(RIGHT*0.75), reverse=True), Write(M[2].next_to(M[1], DOWN), reverse=True), Write(M[3].next_to(M[2], DOWN), reverse=True), Write(M[4].next_to(M[3], DOWN), reverse=True), Write(M[5].next_to(M[4], DOWN).shift(LEFT*0.75), reverse=True), Write(M[6].next_to(M[5], DOWN), reverse=True), runtime=8)
        Mbox = SurroundingRectangle(M, color=PURPLE)
        self.play(Create(Mbox))
        self.play(M.animate.shift(LEFT*2), Mbox.animate.shift(LEFT*2))