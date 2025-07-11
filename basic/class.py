class car:
    def __init__(self,a,b,c,has_sunroof,type):
        self.max_speed = a
        self.company = b
        self.model = c
        self.has_sunroof = has_sunroof
        self.type = type

my = car(200,"Kia","Seltos - E",False,"SUV")
print(my.company)