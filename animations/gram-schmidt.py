from manim import *
from numpy import sqrt


class GramSchmidt(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        self.move_camera(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.play(FadeIn(axes))

        # Create vectors
        v1 = Vector([-1, 1, 2], color=RED)
        v2 = Vector([1, 3, 0], color=BLUE)
        v3 = Vector([2, 1, 1], color=GREEN)

        self.play(GrowArrow(v1), GrowArrow(v2), GrowArrow(v3))
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)

        v1_coords = MathTex(
            r"{{ \mathbf{v_1} }} = {{ \begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix} }}",
            color=RED)
        v2_coords = MathTex(
            r"\mathbf{v_2} = \begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}",
            color=BLUE)
        v3_coords = MathTex(
            r"\mathbf{v_3} = \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}",
            color=GREEN)

        v1_coords.to_corner(UP + RIGHT)
        self.add_fixed_in_frame_mobjects(v1_coords)
        self.play(Write(v1_coords))
        v1.generate_target()
        v1_coords.generate_target()
        v1_coords.target.become(
            MathTex(r"{{ \mathbf{v_1} }} = {{ \frac{1}{\sqrt{6}} }} {{ \begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix} }}",
                    color=RED).move_to(v1_coords)
        )
        v1.target.become(
            Vector([-1 / sqrt(6), 1 / sqrt(6), 2 / sqrt(6)], color=RED)
        )
        self.play(MoveToTarget(v1), MoveToTarget(v1_coords))

        self.wait(2)
