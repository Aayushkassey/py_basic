class Shape:
    """ Class to represent a shape.

    Attributes:
        length: length of the shape
        breadth: Breadth of the shape

    Methods:
        area: claculate area of the shape
        perimeter: calculates perimeter of the shape
    """
    Count= 0
    def __init__(self, l=None,b=None):
        if not l or not b:
            self.length= int(input("Enter the length:"))
            self.breadth= int(input("Enter the breadth:"))
        else:
            self.length = l
            self.breadth = b

        Shape.Count += 1    
        print("Shape has been initiated")
        print("Total Shape:", Shape.Count)

    def __del__(self):
        print("Shape has been deleted")
        Shape.Count -= 1
        print("Total shapes: ", Shape.Count)

    @property
    def area(self):
        
        print('Area is ', self.length*self.breadth)

    @property
    def perimeter(self):
        print('Perimeter is ', 2*(self.length + self.breadth))

shp= Shape(3,5)
shp.length
shp.breadth
shp.area
shp.perimeter

del shp

shp2= Shape(8,9)
shp2.length
shp2.area
shp2.perimeter