from abc import ABC, abstractmethod


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise TypeError


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
    begin = None
    end = None

    def __init__(self, begin, end):
        if isinstance(begin, Point) and isinstance(end, Point):
            self.begin = begin
            self.end = end

    def length(self):
        res = ((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)**0.5
        return res


class Triangle(Figure):
    a = None
    b = None
    c = None
    ab = None
    ac = None
    bc = None

    def __init__(self, p_1, p_2, p_3):
        if isinstance(p_1, Point) and isinstance(p_2, Point) and isinstance(p_3, Point):
            ab_l = self.one_line_length(p_1, p_2)
            ac_l = self.one_line_length(p_1, p_3)
            bc_l = self.one_line_length(p_2, p_3)
            if ab_l + ac_l <= bc_l or ab_l + bc_l <= ac_l or ac_l + bc_l <= ab_l:
                raise ValueError
            else:
                self.a = p_1
                self.b = p_2
                self.c = p_3
                self.ab = ab_l
                self.ac = ac_l
                self.bc = bc_l
        else:
            raise TypeError

    def one_line_length(self, begin, end):
        res = ((end.x - begin.x)**2 + (end.y - begin.y)**2)**0.5
        return res

    def length(self):
        res = self.ab + self.ac + self.bc
        return res

    def area(self):
        res = ((self.length()/2)*(((self.length()/2) - self.ab)*((self.length()/2) - self.ac)*((self.length()/2) - self.bc)))**0.5
        return res


# Normal values:
p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(7, 8)

my_line = Line(p1, p2)

print(my_line.length())
print(my_line.area())

my_triangle = Triangle(p1, p2, p3)

print(my_triangle.length())
print(my_triangle.area())

# Let's crash the Point:
#p4 = Point('1', 0)

# Let's crash the Line:
#line_crash = Point(p1, 'p3')

# Let's crash the Triangle:
#p5 = Point(0, 0)
#p6 = Point(4, 8)
#p7 = Point(8, 16)

#triangle_crash = Triangle(p5, p6, p7)

# Let's crash the Triangle other way:
#triangle_crash2 = Triangle('p8', 1, 2)