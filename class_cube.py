class cube:
    def __init__(self,side):
        self.side=side
    def volume(self):
        return self.side*self.side*self.side
    def surface_area(self):
        return 6*self.side*self.side

a=cube(3)
print(a.volume())
print(a.surface_area())