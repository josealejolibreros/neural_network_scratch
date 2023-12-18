class Component:
    def __init__(self, value):
        self.value = value
        self.a_obj = None
        self.b_obj = None
        self.x = None

    def __add__(self, other):
        if isinstance(other, Component):
            new = Component(self.value + other.value)
            new.a_obj = self.a_obj
            new.x = self.x
            new.b_obj = other
            return new
        else:
            raise TypeError("Unsupported operand type for +: 'MyClass' and '{}'".format(type(other).__name__))

    def __mul__(self, x):
        new = Component(self.value * x)
        new.a_obj = self
        new.x = x
        return new

    def derivate(self, respectto):
        if self.x is None:
            
            if self.a_obj is None:
                return 0

            elif respectto=="b":
                return self.a_obj
            elif respectto=="a":
                return self.b_obj
        elif self.x is not None:
            if respectto=="x":
                return self.a_obj
            elif respectto=="a":
                return self.x
            elif respectto=="b":
                return self.b_obj
        

    def __str__(self):
        return "Component(value={}, a={}, b={})".format(self.value if self else None, self.a_obj.value if self.a_obj else None, self.b_obj.value if self.b_obj else None)

# Example usage
obj1 = Component(10)
obj2 = Component(30)
obj3 = Component(20)
x1=2
x2=3
result1 = obj1*x1
print(result1)
result2 = result1 + obj2
print(result2)
result3 = result2*x2 + obj3
print(result3)
print(result3.derivate(respectto="x"))
print(result3.derivate(respectto="a"))
print(result3.derivate(respectto="b"))
