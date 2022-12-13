from abc import ABC, abstractmethod


class Point:
    _x = None
    _y = None

    def __init__(self, val1, val2):
        self.x = val1
        self.y = val2

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError
        self._y = value


class Figure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def area(self):
        pass

    @abstractmethod
    def length(self):
        pass


class Line(Figure):
    _begin = None
    _end = None

    def __init__(self, be, en):
        self.begin = be
        self.end = en

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._begin = value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._end = value

    def length(self):
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res


class Triangle(Figure):
    _a = None
    _b = None
    _c = None
    _ab = None
    _ac = None
    _bc = None

    def __init__(self, p_1, p_2, p_3):
        self.a = p_1
        self.b = p_2
        self.c = p_3
        self.ab = self.one_line_length(p_1, p_2)
        self.ac = self.one_line_length(p_1, p_3)
        self.bc = self.one_line_length(p_2, p_3)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if not isinstance(value, Point):
            raise TypeError
        self._c = value

    def __str__(self):
        res = f'{self.a.x}, {self.a.y} -- {self.b.x}, {self.b.y} -- {self.c.x}, {self.c.y}'
        return res

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def one_line_length(self, begin, end):
        res = ((end.x - begin.x)**2 + (end.y - begin.y)**2)**0.5
        return res

    def length(self):
        res = self.ab + self.ac + self.bc
        return res

    def area(self):
        res = ((self.length()/2)*(((self.length()/2) - self.ab)*((self.length()/2) - self.ac)*((self.length()/2) - self.bc)))**0.5
        return res


p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(7, 8)

#my_line = Line(p1, p2)

#print(my_line.length())
#print(my_line.area())

my_triangle = Triangle(p1, p2, p3)

#print(my_triangle.length())
#print(my_triangle.area())
print(str(my_triangle))

p5 = Point(0, 0)
p6 = Point(3, 4)
p7 = Point(15, 18)

triangle_big = Triangle(p5, p6, p7)

print(triangle_big <= my_triangle)
