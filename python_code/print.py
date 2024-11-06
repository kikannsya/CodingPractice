class foo:
    def __init__(self, x, y) -> None:
        self.x =  x
        self.y = y
    
    # return str object for print()
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
    
    # return str object for repr()
    def __repr__(self):
        return f'foo({self.x}, {self.y})'

p = foo(1, 3)
print('p: ', p)

# eval(str), perform str as python code
p1 = eval(repr(p))
print('p1: ',p1)