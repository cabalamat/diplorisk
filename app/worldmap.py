# worldmap.py = a world map

import random


from utils import butil
from utils.butil import form

import wentity

#---------------------------------------------------------------------

squares = wentity.WEntityManager("square")

class Square(wentity.WEntity):
    """ a square on a map """

    wid: str # web id
    isLand: bool = True # is land
    name: str = "" # name of this square

    def __init__(self, wid):
        self.wid = wid
        squares.add(self)

    @classmethod
    def entityType(cls) -> str:
        return "square"

    def tdh(self):
        """ the representation of this square as a td (inside a table) """
        h = form("<td style='background:{}'>", self.bgCol())
        h += self.a()
        if self.isLand:
            h += "<br>" + self.name
        h += "</td>"
        return h

    #===== for html output

    def bgCol(self) -> str:
        """ background colour """
        return "#ccffcc" if self.isLand else "#cceeff"

    def longName(self) -> str:
        return self.name if self.isLand else ""

def makeRandomName() -> str:
    """ make a random name for a square """
    nameLen = random.choice([1,2,2,3])
    name = ""
    for _ in range(nameLen):
        s1 = random.choice("p b t d k g f v s z h".split() + [""])
        s2 = random.choice("r y w l".split() + [""]*8)
        vowel = random.choice("i e a o u ai ei oi au".split())
        s3 = random.choice("p b t d k g f v s z".split() + [""]*6)
        syl = s1 + s2 + vowel + s3
        name += syl
    #//for _
    return name[0].upper() + name[1:]

def makeSquare(rix: int, cix: int) -> Square:
    """ make a random Square """
    wid = "%02d%02d" % (rix, cix)
    sq = Square(wid)
    if random.random() < 0.5:
        sq.isLand = False # make it sea
        sq.name = wid
    else:
        sq.name = makeRandomName()
    return sq

#---------------------------------------------------------------------

class WorldMap:

    rows: int # number of rows in map
    cols: int # number of columns in map
    squares: list[list[Square]] = []

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.squares = []
        for r in range(rows):
            theRow = []
            for c in range(cols):
                theRow.append(makeSquare(r, c))
            #//for c
            self.squares.append(theRow)
        #//for r


    def h(self) -> str:
        """ return an html representation """
        h = "<table class='map'>\n"
        for row in self.squares:
            h += "<tr>\n"
            for sq in row:
                h += form("  {}\n", sq.tdh())
            #//for sq
            h += "</tr>\n"
        #//for row
        h += "</table>\n"
        return h


worldMap = WorldMap(rows=8, cols=12)

#---------------------------------------------------------------------

def randNames():
    print("some random names:")
    for i in range(10):
        print(makeRandomName())



#end
