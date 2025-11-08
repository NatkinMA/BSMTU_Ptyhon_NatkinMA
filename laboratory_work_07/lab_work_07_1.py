from math import sqrt
import turtle as tr


class CoordinateSystem:
    @staticmethod
    def __plot_axis(self, min_value, max_value, ax="X"):
        tr.up()
        if ax == "X":
            begin = (min_value, 0)
            end = (max_value, 0)
        else:
            begin = (0, min_value)
            end = (0, max_value)
        tr.goto(begin)
        tr.down()
        tr.goto(end)

    @staticmethod
    def __plot_mark(self, min_value, max_value, ax="X"):
        tr.up()
        for t in range(min_value, max_value):
            if ax == "X":
                point_begin = (t, 0)
                point_end = (t, 0.2)
                point_width = (t, -0.5)
            else:
                point_begin = (0, t)
                point_end = (0.2, t)
                point_width = (-0.5, t)
            tr.goto(point_begin)
            tr.down()
            tr.goto(point_end)
            tr.up()
            tr.goto(point_width)
            tr.write(str(t), font=("Arial", 14, "bold"))

    @staticmethod
    def __plot_arrow(self, max_value, ax="X"):
        triangle = [(0.1, -0.1), (0, 0.3), (-0.1, -0.1)]
        tr.up()
        tr.goto(0, 0)
        tr.begin_poly()
        for couple in triangle:
            tr.goto(couple)
        tr.end_poly()
        arrow = tr.get_poly()
        tr.register_shape("myArrow", arrow)
        tr.resizemode("myArrow")
        tr.shapesize(1, 2, 1)
        if ax == "X":
            tr.tiltangle(0)
            tr.goto(max_value + 0.2, 0)
            point_width = (int(max_value), -1.0)
        else:
            tr.tiltangle(90)
            tr.goto(0, max_value + 0.2)
            point_width = (0.2, int(max_value))
        tr.stamp()
        tr.goto(point_width)
        tr.write(ax, font=("Arial", 14, "bold"))

    def __init__(self,  title, axis_X, axis_Y, Dx=1000):
        self.axis_X = axis_X
        self.axis_Y = axis_Y
        self.Dx = Dx
        self.Dy = int(Dx / ((axis_X[1] - axis_X[0]) / (axis_Y[1] - axis_Y[0])))
        self.title = title

        tr.setup(self.Dx, self.Dy)
        tr.reset()

        tr.setworldcoordinates(axis_X[0], axis_Y[0], axis_X[1], axis_Y[1])

        tr.title(title)
        tr.width(2)
        tr.color("blue", "blue")

        tr.ht()
        tr.tracer(0, 0)

        self.__plot_axis(self, axis_X[0], axis_X[1], "X")
        self.__plot_mark(self, axis_X[0], axis_X[1], "X")
        self.__plot_arrow(self, axis_X[1], "X")

        self.__plot_axis(self, axis_Y[0], axis_Y[1], "Y")
        self.__plot_mark(self, axis_Y[0], axis_Y[1], "Y")
        self.__plot_arrow(self, axis_Y[1], "Y")


class Function(CoordinateSystem):
    @staticmethod
    def function(x):
        y = 0.0
        if x < -5:
            y = 1
        elif -5 <= x < 0:
            y = -(3 / 5) * x - 2
        elif 0 <= x < 2:
            y = -sqrt(4 - x ** 2)
        elif 2 <= x < 4:
            y = x - 2
        elif 4 <= x < 8:
            y = 2 + sqrt(4 - (x - 6) ** 2)
        elif x >= 8:
            y = 2
        return y

    def plot_function(self, min_value, max_value, color="red", n_max=1000):
        tr.color(color)
        tr.width(3)
        dx = (max_value - min_value) / n_max

        x = min_value
        y = self.function(x)
        if y is None:
            tr.up()
            tr.goto(x, y)
        else:
            tr.goto(x, y)
            tr.down()
        while x <= max_value:
            x = x + dx
            y = self.function(x)
            if y is None:
                tr.up()
                continue
            else:
                tr.goto(x, y)
                tr.down()

    def __init__(self, title, axis_X, axis_Y, color, Dx):
        super().__init__(title, axis_X, axis_Y, Dx)

        self.plot_function(axis_X[0], axis_X[1], color, Dx)

        tr.mainloop()


if __name__ == "__main__":
    myFunction = Function("lab_work_7_1", (-10, 10), (-5, 5), "red", 1000)
