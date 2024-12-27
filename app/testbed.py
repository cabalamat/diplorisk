# testbed.py = various testing


#---------------------------------------------------------------------


print("===== fields in a class =====")

class Foo:
    a: int = 0
    b: str = "hello"
    c: list[str] = []

class Bar(Foo):
    d: bool

f = Foo()
print("Foo's data: ", Foo.__annotations__)
print("Bar's data: ", Bar.__annotations__)
print("Bar's direct superclasses: ", Bar.__bases__)


#---------------------------------------------------------------------


#end
