from math import tan, cos, sin, pi, log

def function_1(a, x):
    return tan(x**2/2-1)**2+(2*cos(x-pi/6))/(1/2+sin(a)**2)

def function_2(x):
    return pow(2, log(3-cos(pi/4+2*x), 3+sin(x))/(1+tan(2*x/pi)**2))

with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        header = "  a     x     y1     y2"
        print(header)
        output_file.write(header + "\n")
        for line in input_file:
            a, x = line.split()
            output_line = "{0:.2f} {1:.2f} {2:.4f} {3:.4f}".format(float(a),
                                                    float(x),
                                                    function_1(float(a), float(x)),
                                                    function_2(float(x)))
            print(output_line)
            output_file.write(output_line + "\n")
