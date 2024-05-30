class Cookie:
    def __init__(self, color):
        
        self.set_color(color)

    def get_color(self):
        return self._color
    
    def set_color(self, color):
        if isinstance(color, str):
            self._color = color
        else:
            raise ValueError("Color must be a string.")
    @classmethod
    def from_number(cls, num):
        match num:
            case 1:
                return cls("red")
            case 2:
                return cls("blue")
            case 3:
                return cls("yellow")
            case 4:
                return cls("black")
            case _:
                return cls("white")
        

     
cookie_one = Cookie("green")
cookie_two = Cookie.from_number(2)
print(cookie_two.get_color())

