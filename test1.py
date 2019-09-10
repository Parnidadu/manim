from manimlib.imports import *

class Shapes(Scene):
    def construct(self):
        ######Code######
        #Making shapes
        circle = Circle()
		cube = Cube()
		arrow = Arrow(RIGHT)
        square1 = Square(fill_color = blue)
		square2 = Square(fill_color = blue)
		square3 = Square(fill_color = blue)
		square4 = Square(fill_color = blue)
		square5 = Square(fill_color = blue)
		square6 = Square(fill_color = blue)
	#placing squares
		square1.move_to(UP+RIGHT)
		square2.next_to(square1,LEFT)
		square3.next_to(square1,RIGHT)
		square4.next_to(square1,UP)
		square5.next_to(square1,DOWN)
		square6.next_to(square5,DOWN)
        #triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        #Showing shapes
		self.add(cube)
		self.play(GrowArrow(arrow))
        #self.play(ShowCreation(circle))
        #self.play(FadeOut(circle))
        #self.play(GrowFromCenter(square))
#squares in its shape
        self.play(square1)
		self.play(square2)
		self.play(square3)
		self.play(square4)
		self.play(square5)
		self.play(square6)
	
