from manimlib.imports import *
from math import cos, sin, pi

class Shapes(Scene):
    def construct(self):
        #######Code#######
        #Making Shapes
        cube = Cube()
        square = Square(size=0.1)
        
        #arrow = Arrow()
        square1 = Square(size=1)
        square2 = Square(size=1)
        square3 = Square(size=1)
        square4 = Square()
        square5 = Square()
        #placing squares and cubes
        cube.move_to(3*LEFT)
        square.move_to(UP+2*RIGHT)
        square1.next_to(square,LEFT)
        square2.next_to(square,RIGHT)
        square3.next_to(square,UP)
        square4.next_to(square,DOWN)
        square5.next_to(square4,DOWN)
		
        #changing camera  orientation
        #self.set_camera_orientation(0.6, -0.7853981, 86.6)
    #showing shapes
        self.play(ShowCreation(cube))
        #self.play(arrow)
        self.play(FadeIn(square))
        #self.play(GrowArrow(arrow))
        self.play(FadeIn(square1))
        self.play(FadeIn(square2))
        self.play(FadeIn(square3))
        self.play(FadeIn(square4))
        self.play(FadeIn(square5))
        #self.move_camera(0.8*np.pi/2, -0.45*np.pi)
        self.wait(2)    
