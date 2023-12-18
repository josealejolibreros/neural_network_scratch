class Component:
    def __init__(self, value):
        self.value = value
        self.a_obj = None
        self.b_obj = None
        self.h_obj = None
        self.x = None

    def __add__(self, other):
        if isinstance(other, Component):
            new = Component(self.value + other.value)
            new.a_obj = self
            new.b_obj = other
            return new
        else:
            raise TypeError("Unsupported operand type for +: 'MyClass' and '{}'".format(type(other).__name__))

    def derivate(self, respectto):
        if self.x is None:
            
            if self.a_obj is None:
                return 0

            elif respectto=="b":
                return self.a_obj
            elif respectto=="a":
                return self.b_obj
        elif respectto=="x":
            return self.h_obj

    def __str__(self):
        return "Component(value={}, a={}, b={})".format(self.value if self else None, self.a_obj.value if self.a_obj else None, self.b_obj.value if self.b_obj else None)

# Example usage
obj1 = Component(10)
obj2 = Component(30)

result = obj1 + obj2
print(result)  # This will print: MyClass(a=10, b=30)
