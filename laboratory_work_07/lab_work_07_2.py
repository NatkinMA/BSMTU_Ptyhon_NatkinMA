import turtle as tr
from random import uniform
from lab_work_07_1 import CoordinateSystem


class Figure(CoordinateSystem):
    @staticmethod
    def function_1(x):
        return 2 * x + 2

    @staticmethod
    def function_2(x):
        return x ** 3 - 4 * x ** 2 + x + 6

    def is_hit(self, x, y):
        if (-1 <= x <= 4) and \
                (self.function_1(x) <= y <= self.function_2(x) or
                 self.function_1(x) >= y >= self.function_2(x)):
            return True
        return False

    def __init__(self, title, axis_X, axis_Y, color, Dx, shots):
        super().__init__(title, axis_X, axis_Y, Dx)

        tr.color(color)
        tr.shape("circle")
        tr.resizemode("circle")
        tr.shapesize(0.2, 0.2, 0.2)

        mfun = 0

        for shot in range(shots):
            x = uniform(axis_X[0], axis_X[1])
            y = uniform(axis_Y[0], axis_Y[1])

            tr.goto(x, y)

            if self.is_hit(x, y):
                tr.dot(5, color)
                mfun += 1
            else:
                tr.dot(5, "pink")

        Sf = (axis_X[1] - axis_X[0]) * (axis_Y[1] - axis_Y[0]) * mfun / shots
        tr.goto(1, 9)
        tr.color("blue")
        tr.write("N = {0:8d}\nNf = {1:8d}\nSf = {2:8.2f}".format(shots, mfun, Sf),
                 font=("Arial", 14, "bold"))
        tr.mainloop()


if __name__ == "__main__":
    myFigure = Figure("lab_work_7_2", (-2, 5), (-2, 11), "green", 500, 10000)
