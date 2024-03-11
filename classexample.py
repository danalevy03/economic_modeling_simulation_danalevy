class Point:
    # all classes need to have an init method
    def __init__(self, x, y):
        # init method that initialized the point with X and Y
        # :param x: x-coordinate
        # :param y: y-coordinate
        self.x = x
        self.y = y

    def __str__(self): #how to print this point?
        return f'<x={self.x},y= {self.y}>'

    def __repr__(self): # how to print if in a list?
        return self.__str__()

    def distance_origin(self): #return the distance from the origin to the point
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __gt__(self, other): #how to compare 2 points? we define it here!
       # return self.distance_origin() > other.distance_origin()
        my_size = self.distance_origin()
        other_size = other.distance_origin()
        return my_size > other_size

    def __eq__(self, other):
        return self.distance_origin() == other.distance_origin()

    if __name__ == "__main__":


        a = Point(2,3) # Instantiate by calling the name of the class and parameters in brackets

        #print(a.x) # 2
        #print(a.y) # 3

        b = Point(7,9)
        #print(b.x, b.y) # 7 9


        # add 5 random points into a list
        import random

        points = []
        for i in range(5):
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            points.append(Point(x, y))

        for point in points:
            print(point.x, point.y)

        # professor's solution

        for _ in range(5):
            points.append(Point(random.randint(0, 100), random.randint(0, 100)))

        for point in points:
            print(point)

        print(points)
        a = Point(3, 4) #we expect 5 as distance to origin
        b = Point(12, 5) #we expect 13 as distance to origin
        c = Point(5, 12) #we expect 5 as distance to origin

        print(a.distance_origin(), b.distance_origin())
        print(a < b)
        print(b < a)
        print(b == c)
        points.sort()
        print(f"the biggest point is {points[-1]} and the smallest point is: {points[0]}")



