from manim import *
from numpy import sqrt

RES = 16


class GramSchmidt(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        self.move_camera(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.play(FadeIn(axes))

        # Create vectors
        v1 = Arrow3D(ORIGIN, [-1, 1, 2], resolution=RES,
                     height=0.1, color=RED, z_index=0)
        v2 = Arrow3D(ORIGIN, [1, 3, 0], resolution=RES,
                     height=0.1, color=BLUE, z_index=0)
        v3 = Arrow3D(ORIGIN, [2, 1, 1], resolution=RES,
                     height=0.1, color=GREEN, z_index=0)

        self.play(Create(v1), Create(v2), Create(v3))
        self.move_camera(phi=45 * DEGREES, theta=15 * DEGREES)

        self.wait(1)
        v1.generate_target()
        v1.target.become(
            Arrow3D(ORIGIN, [-1 / sqrt(6), 1 /
                    sqrt(6), 2 / sqrt(6)], resolution=RES, height=0.1, color=RED,
                    z_index=0)
        )
        self.play(MoveToTarget(v1))

        self.wait(1)

        v1_line = Line3D(-4 * v1.get_end(), 4 * v1.get_end(),
                         thickness=0.01, resolution=RES, color=GOLD, z_index=-1)
        self.play(Create(v1_line))

        perp_line = Line3D.perpendicular_to(
            v1_line, v2.get_end(), length=10, resolution=RES, thickness=0.01,
            color=GOLD, z_index=-1)
        self.play(Create(perp_line))

        self.wait(1)
        w2 = Arrow3D(ORIGIN, [-1 / 3, 1 / 3, 2 / 3],
                     resolution=RES, height=0.1, thickness=0.03, color=TEAL,
                     z_index=1)
        self.play(Create(w2))

        self.wait(1)
        w2.generate_target()
        w2.target.become(
            Arrow3D(v2.get_end(), v2.get_end() - w2.get_end(), resolution=RES,
                    height=0.1, color=TEAL, z_index=1)
        )
        self.play(MoveToTarget(w2))

        u2 = Arrow3D(ORIGIN, v2.get_end() - w2.get_end(), resolution=RES,
                     height=0.1, color=YELLOW, z_index=1)
        self.play(Create(u2))

        self.wait(1)
        u2.generate_target()
        u2.target.become(
            Arrow3D(ORIGIN, [2 / sqrt(21), 4 / sqrt(21), -1 / sqrt(21)],
                    resolution=RES, height=0.1, color=YELLOW, z_index=1)
        )
        self.play(MoveToTarget(u2), FadeOut(perp_line),
                  FadeOut(v1_line), FadeOut(w2), FadeOut(v2))

        self.wait(1)
        plane = Surface(
            lambda u, v: axes.c2p(-u + 2*v, u + 4 * v, 2 * u - v),
            u_range=(-2, 2), v_range=(-2, 2),
            resolution=RES,
            fill_color=WHITE,
            fill_opacity=0.3,
            checkerboard_colors=None
        )
        self.play(Create(plane))
        self.move_camera(phi=105 * DEGREES, theta=45 * DEGREES)

        w3_line = Line3D(ORIGIN, [1, 3, 0])
        perp_line = Line3D.perpendicular_to(
            w3_line, v3.get_end(),
            length=10, resolution=RES,
            thickness=0.01, color=GOLD,
            z_index=-1
        )
        self.play(Create(perp_line))

        self.wait(1)
        w3 = Arrow3D(ORIGIN, [1 / 2, 3 / 2, 0],
                     resolution=RES, height=0.1, thickness=0.03, color=TEAL,
                     z_index=1)
        self.play(Create(w3))

        self.wait(1)
        w3.generate_target()
        w3.target.become(
            Arrow3D(v3.get_end(), v3.get_end() - w3.get_end(), resolution=RES,
                    height=0.1, color=TEAL, z_index=0)
        )
        self.play(MoveToTarget(w3))

        u3 = Arrow3D(ORIGIN, v3.get_end() - w3.get_end(), resolution=RES,
                     height=0.1, color=PINK, z_index=1)
        self.play(Create(u3))

        self.wait(1)
        u3.generate_target()
        u3.target.become(
            Arrow3D(ORIGIN, [3 / sqrt(14), -1 / sqrt(14), 2 / sqrt(14)],
                    resolution=RES, height=0.1, color=PINK, z_index=0)
        )
        self.play(MoveToTarget(u3), FadeOut(perp_line),
                  FadeOut(w3), FadeOut(v3), FadeOut(plane))

        self.wait(2)


class GramSchmidtText(Scene):
    def construct(self):
        v1_coords = VGroup(*[
            MathTex(r"\mathbf{v_1}", color=RED),
            MathTex("=", color=WHITE),
            MathTex(r"\begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix}", color=RED)
        ]).arrange(RIGHT)

        self.play(Write(v1_coords))
        self.wait(1)
        v1_coords.generate_target()
        v1_coords.target += MathTex(r"\frac{1}{\sqrt{6}}", color=RED)
        (v1_coords.target[-1], v1_coords.target[-2]
         ) = (v1_coords.target[-2], v1_coords.target[-1])
        v1_coords.target[0] = MathTex(r"\mathbf{u_1}", color=RED)
        v1_coords.target.arrange(RIGHT)

        self.play(MoveToTarget(v1_coords))

        v1_coords.generate_target()
        v1_coords.target[-1] = MathTex(r"(-1, 1, 2)^T", color=RED)
        v1_coords.target.arrange(RIGHT).shift(2 * UP)
        self.play(MoveToTarget(v1_coords))

        self.wait(1)
        v2_coords = VGroup(*[
            MathTex(r"\mathbf{v_2}", color=BLUE),
            MathTex("=", color=WHITE),
            MathTex(r"\begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}", color=BLUE)
        ]).arrange(RIGHT)
        self.play(Write(v2_coords))
        w2_coords = VGroup(*[
            MathTex(r"\rightarrow", color=WHITE),
            MathTex(r"\mathbf{w_2}", color=TEAL),
            MathTex("=", color=WHITE),
            MathTex(r"{{ \langle }} \mathbf{u_1} {{ , }} \mathbf{v_2} {{ \rangle }} \mathbf{u_1}",
                    tex_to_color_map={
                        r"\mathbf{u_1}": RED,
                        r"\mathbf{v_2}": BLUE
                    },
                    color=WHITE)
        ]).arrange(RIGHT).next_to(v2_coords, RIGHT)
        v2_w2 = VGroup(v2_coords, w2_coords)
        self.play(FadeIn(w2_coords, shift=RIGHT),
                  v2_w2.animate.move_to(ORIGIN))

        self.wait(1)
        w2_calc = VGroup(*[
            MathTex(r"\mathbf{w_2}", color=TEAL),
            MathTex("=", color=WHITE),
            MathTex((r"{{ \frac{1}{6} \left\langle }}"
                     r"\begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix}"
                     r"{{ , }}"
                     r"\begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}"
                     r"{{ \right\rangle }}"
                     r"\begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix}"),
                    tex_to_color_map={
                r"\begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix}": RED,
                r"\begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}": BLUE
            },
                color=WHITE)
        ]).arrange(RIGHT).next_to(v2_w2, DOWN)
        self.play(Write(w2_calc))
        w2_final = VGroup(*[
            MathTex(r"=", color=WHITE),
            MathTex(
                r"\frac{1}{3} \begin{pmatrix} -1 \\ 1 \\ 2 \end{pmatrix}",
                color=TEAL)
        ])
        w2_final.arrange(RIGHT).next_to(w2_calc, RIGHT)
        w2_calc.add(w2_final)

        self.play(FadeIn(w2_final, shift=RIGHT),
                  w2_calc.animate.next_to(v2_w2, DOWN))

        self.wait(1)
        w2_calc.generate_target()
        w2_calc.target.become(
            MathTex(r"{{ \mathbf{w_2} }} = {{ \frac{1}{3} (-1, 1, 2)^T }}",
                    tex_to_color_map={
                        r"\mathbf{w_2}": TEAL,
                        r"\frac{1}{3} (-1, 1, 2)^T": TEAL
                    }, color=WHITE)
        )
        w2_calc.target.next_to(v1_coords, DOWN, aligned_edge=LEFT)

        self.play(MoveToTarget(w2_calc), FadeOut(v2_w2))

        self.wait(1)

        v2_minus_w2 = MathTex(r"\mathbf{v_2}",
                              r"-",
                              r"\mathbf{w_2}",
                              r"=",
                              r"\frac{2}{3}",
                              r"\begin{pmatrix} 2 \\ 4 \\ -1 \end{pmatrix}",
                              tex_to_color_map={
                                  r"\mathbf{v_2}": BLUE,
                                  r"\mathbf{w_2}": TEAL
                              }, color=WHITE).next_to(w2_calc, DOWN)
        self.play(Write(v2_minus_w2))

        self.wait(1)
        u2_coords = MathTex(
            r"\mathbf{u_2}", r"=",
            r"{",
            r"\mathbf{v_2}",
            r"-",
            r"\mathbf{w_2}",
            r"\over \|",
            r"\mathbf{v_2}",
            r"-",
            r"\mathbf{w_2}"
            r"\|}",
            tex_to_color_map={
                r"\mathbf{v_2}": BLUE,
                r"\mathbf{w_2}": TEAL,
                r"\mathbf{u_2}": YELLOW
            }, color=WHITE).next_to(v2_minus_w2, DOWN)

        self.play(FadeIn(u2_coords, shift=DOWN))

        u2_final = MathTex(r"=", r"{1 \over \sqrt{21}} \begin{pmatrix} 2 \\ 4 \\ -1 \end{pmatrix}",
                           tex_to_color_map={
                               r"=": WHITE,
                           }, color=YELLOW).next_to(u2_coords, RIGHT)
        u2_coords.add(u2_final)
        self.play(FadeIn(u2_final, shift=RIGHT),
                  u2_coords.animate.next_to(v2_minus_w2, DOWN))

        self.wait(1)
        u2_coords.generate_target()
        u2_coords.target.become(
            MathTex(r"\mathbf{u_2}",
                    r"=",
                    r"{1 \over \sqrt{21}}",
                    r"(2, 4, -1)^T",
                    tex_to_color_map={
                        r"\mathbf{u_2}": YELLOW,
                        r"1 \over \sqrt{21}": YELLOW,
                        r"(2, 4, -1)^T": YELLOW
                    }, color=WHITE)
        ).next_to(v1_coords, DOWN, aligned_edge=LEFT)
        self.play(MoveToTarget(u2_coords), FadeOut(
            v2_minus_w2), FadeOut(w2_calc))

        self.play(v1_coords.animate.shift(UP), u2_coords.animate.shift(UP))

        self.wait(1)

        v3_coords = MathTex(
            r"\mathbf{v_3}", r"=", r"(2, 1, 1)^T",
            tex_to_color_map={
                r"\mathbf{v_3}": GREEN,
                r"(2, 1, 1)^T": GREEN
            }, color=WHITE).next_to(u2_coords, DOWN)

        self.play(Write(v3_coords))

        w3_calc = MathTex(
            r"\mathbf{w_3}",
            r"=",
            r"\langle",
            r"\mathbf{u_1}",
            r","
            r"\mathbf{v_3}",
            r"\rangle",
            r"\mathbf{u_1}",
            r"+",
            r"\langle",
            r"\mathbf{u_2}",
            r",",
            r"\mathbf{v_3}",
            r"\rangle",
            r"\mathbf{u_2}",
            tex_to_color_map={
                r"\mathbf{u_1}": RED,
                r"\mathbf{u_2}": YELLOW,
                r"\mathbf{v_3}": GREEN,
                r"\mathbf{w_3}": TEAL
            }, color=WHITE).next_to(v3_coords, DOWN)

        self.play(Write(w3_calc))

        self.wait(1)
        w3_final = MathTex(
            r"=", r"{1 \over 2} (1, 3, 0)^T",
            tex_to_color_map={
                r"=": WHITE,
            }, color=TEAL).next_to(w3_calc, RIGHT)

        w3_calc.add(w3_final)
        self.play(FadeIn(w3_final, shift=RIGHT), w3_calc.animate.next_to(
            v3_coords, DOWN))

        v3_minus_w3 = MathTex(
            r"\mathbf{v_3}", r"-", r"\mathbf{w_3}",
            r"=", r"\frac{1}{2}", r"(3, 1, -2)^T",
            tex_to_color_map={
                r"\mathbf{v_3}": GREEN,
                r"\mathbf{w_3}": TEAL
            }, color=WHITE).next_to(w3_calc, DOWN)
        self.play(Write(v3_minus_w3))

        self.wait(1)
        u3_coords = MathTex(
            r"\mathbf{u_3}", r"=",
            r"{", r"\mathbf{v_3}", r"-", r"\mathbf{w_3}", r"\over \|",
            r"\mathbf{v_3}", r"-", r"\mathbf{w_3}", r"\|}",
            tex_to_color_map={
                r"\mathbf{v_3}": GREEN,
                r"\mathbf{w_3}": TEAL,
                r"\mathbf{u_3}": PINK
            }, color=WHITE).next_to(v3_minus_w3, DOWN)

        self.play(FadeIn(u3_coords, shift=DOWN))

        u3_final = MathTex(
            r"=", r"{1 \over \sqrt{14}} (3, 1, -2)^T",
            tex_to_color_map={
                r"=": WHITE,
            }, color=PINK).next_to(u3_coords, RIGHT)
        u3_coords.add(u3_final)

        self.play(FadeIn(u3_final, shift=RIGHT), u3_coords.animate.next_to(
            v3_minus_w3, DOWN))

        self.wait(1)

        u3_coords.generate_target()
        u3_coords.target.become(
            MathTex(r"\mathbf{u_3}", r"=",
                    r"{1 \over \sqrt{14}}", r"(3, 1, -2)^T",
                    tex_to_color_map={
                        r"\mathbf{u_3}": PINK,
                        r"1 \over \sqrt{14}": PINK,
                        r"(3, 1, -2)^T": PINK
                    }, color=WHITE)
        ).next_to(u2_coords, DOWN, aligned_edge=LEFT)
        self.play(MoveToTarget(u3_coords), FadeOut(
            v3_minus_w3), FadeOut(w3_calc), FadeOut(v3_coords))

        self.wait(2)
