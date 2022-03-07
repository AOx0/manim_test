import time

import manim.animation.transform
from manim import *
from manim.animation.creation import Write


class DefaultTemplate(Scene):
    def construct(self):
        self: Scene

        texto = Text("Resolver por Gauss-Jordan")

        self.play(Write(texto))

        self.wait(0.2)

        self.play(FadeOut(texto))

        tex = MathTex(r"""
            x + 2y -z &= 9  \\
            2x - y + 3z &= -2  \\
            3x - 3y - 4z &= 1
        """)
        self.play(Write(tex))

        tex2 = MathTex(r"""
           \left( \begin{array}{rrr|r}
     1 & 2 & -1 & 9 \\
     2 & -1 & 3 & -2 \\
     3 & -3 & -4 & 1
  \end{array} \right)
        """)
        self.play(manim.animation.transform.FadeTransform(tex, tex2))

        tex3 = MathTex(r"""
         \left( \begin{array}{rrr|r}
             1 & 2 & -1 & 9 \\
             2 & -1 & 3 & -2 \\
             3 & -3 & -4 & 1
          \end{array} \right)
                """)
        self.play(manim.animation.transform.FadeTransform(tex2, tex3))

        self.play(tex3.animate.shift([0, -0.5, 0]))

        tex4 = MathTex(r"""
        \left.
             \begin{array}{rrrr}
                 x & \phantom{-} y & \phantom{-} z & \phantom{-} b
              \end{array}
         \right.
        """)

        tex4 = tex4.set_y(tex4.get_y()+1)

        self.play(Write(tex4))

        self.play(FadeOut(tex4), tex3.animate.shift([0, +0.5, 0]))

        self.wait(2)
