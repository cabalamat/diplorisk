# wentity.py = web entity

"""
A Web Entity (instance of WEntity subclass) is an object that has
a url associated with it.

"""

from typing import Optional

#---------------------------------------------------------------------

class WEntityManager:
    """ manages web enetities """

    def get(self, typ: str, wid: str):
        """ return the WEntity for a typ and wid,
        if one exists
        """

    def getForTyp(self, typ: str) -> dict[str, 'WEntity']:
        """ return all the WEntities for a typ, as a dict
        with the wids as keys.
        """

# there's only one manager:
entities = WEntityManager()

#---------------------------------------------------------------------

class WEntity:

    def a(self) -> str:
        """ return HTML for an a href to the entity """

    def url(self) -> str:
        """ return the entity's url """


#---------------------------------------------------------------------

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




#end
