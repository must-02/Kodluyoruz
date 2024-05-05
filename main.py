import math
def main():
    points = [(23,8), (1,-67), (6,459), (-3, -291), (0,0)]
    distances = []

    def euclideanDistance(t1, t2):
        x_axis_length = t1[0] - t2[0]
        y_axis_length = t1[1] - t2[1]

        d_square = pow(x_axis_length, 2) + pow(y_axis_length, 2)
        d = math.sqrt(d_square)
        return d

    for fp in range(len(points)):
        for sp in range(len(points) - fp - 1):
            x = euclideanDistance(points[fp], points[sp + fp + 1])
            distances.append(x.__round__(3))

    print(distances)

if __name__ == '__main__':
    main()

