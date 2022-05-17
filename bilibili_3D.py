#By Wei 2020/6/16
from manimlib.imports import *
import numpy as np
class Test(ThreeDScene):
    #这里我只列举了其中一个，其余类比即可
    def construct(self):
        sphere = ParametricSurface(
        lambda u, v: np.array([
            (np.cos(u)*np.sin(v)*np.sin(v))*3,
            (np.sin(u)*np.cos(v)*np.sin(v))*3,
            (np.cos(u)*np.sin(u)*(np.cos(v))**2)*3
        ]),v_min=0,v_max=TAU,u_min=0,u_max=2*TAU,checkerboard_colors=[RED_D, RED_E],
        resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=65 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.5)

        axes = ThreeDAxes()
        self.add(axes)
        self.play(Write(sphere),run_time=6)
        self.wait(9)

class write_formula(Scene):
    def construct(self):
        formula1 = TexMobject(r"\begin{cases} x=\rho\sin\varphi\cos\theta \\ y=\rho\sin\varphi\sin\theta \\ z=\rho\cos\varphi \\ \end{cases}")
        formula2 = TexMobject(r"\begin{cases} x=R\cos(u)+r\cos(u)\cos(v) \\ y=R\sin(u)+r\sin(u)\cos(v) \\ z=r\sin(v) \\ \end{cases}")
        formula3 = TexMobject(r"\begin{cases} x=u\cos(v) \\ y=u\sin(v) \\ z=u+v \\ \end{cases}")
        formula4 = TexMobject(r"\begin{cases} x=(1+\frac{v}{2}\cos(\frac{u}{2}))\cos(u) \\ y=(1+\frac{v}{2}\cos(\frac{u}{2}))\sin(u) \\ z=\frac{v}{2}\sin(\frac{u}{2}) \\ \end{cases}")
        formula5 = TexMobject(r"\begin{cases} x=(\cos(u)\cos(v))^3 \\ y=(\sin(u)\cos(v))^3 \\ z=(\sin(v))^3 \\ \end{cases}")
        formula6 = TexMobject(r"\begin{cases} x=(1-u)(4+\cos(v))\cos(\frac{\pi{u}}{2}) \\ y=(1-u)(4+\cos(v))\sin(\frac{\pi{u}}{2}) \\ z=4u+(1-u)\sin(v)+\pi \\ \end{cases}")
        formula7 = TexMobject(r"\begin{cases} x=\cos(u)\cos(v)\sin(v) \\ y=\sin(u)\cos(v)\sin(v) \\ z=\cos(u)\sin(u)(\cos(v))^2 \\ \end{cases}")
        self.play(Write(formula1), run_time = 5)
        self.wait()
        self.play(ReplacementTransform(formula1, formula2), run_time = 3)
        self.wait()
        self.play(ReplacementTransform(formula2, formula3), run_time = 3)
        self.wait()
        self.play(ReplacementTransform(formula3, formula4), run_time = 3, path_arc = 3)
        self.wait()
        self.play(ReplacementTransform(formula4, formula5), run_time = 3)
        self.wait()
        self.play(ReplacementTransform(formula5, formula6), run_time = 3, path_arc = 3)
        self.wait()
        self.play(ReplacementTransform(formula6, formula7), run_time = 3)
        self.wait()