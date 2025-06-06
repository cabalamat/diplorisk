# worldmap.py = a world map

import random
random.seed(1234)
from collections.abc import Iterable, Iterator

from utils import butil
from utils.butil import form, kv, sortedKv

import wentity

import config
import resource
from resource import Resource, resourceManager

#---------------------------------------------------------------------

squares = wentity.WEntityManager("square")

class Square(wentity.WEntity):
    """ a square on a map """

    wid: str # web id
    isLand: bool = True # is land
    name: str = "" # name of this square
    theMap: 'WorldMap'
    resources: list[Resource] = []

    def __init__(self, wid, theMap):
        self.wid = wid
        self.theMap = theMap
        squares.add(self)
        self.resources = []

    @classmethod
    def entityType(cls) -> str:
        return "square"

    def getCoords(self) -> tuple[int, int]:
        """ return my row,col coords, taken from wid """
        return (int(self.wid[:2]), int(self.wid[2:4]))

    #===== for html output

    def bgCol(self) -> str:
        """ background colour """
        return "#ccffcc" if self.isLand else "#000000"

    def longName(self) -> str:
        return self.name if self.isLand else ""

    def icon(self)-> str:
        return ("<i class='fas fa-tree'></i> " if self.isLand
                else "<i class='fas fa-water'></i> ")

    def tdh(self):
        """ the representation of this square as a td (inside a table) """
        h = form("<td style='background:{}'>", self.bgCol())

        h += self.a()
        if self.isLand:
            h += " <i class='fa fa-star'></i>"
            h += " <i class='fa fa-flag'></i>"
            h += "<br>" + self.name
        else:
            # empty
            pass

        resH = ""
        for res in self.resources:
            resH += res.a()
        if resH: h += "\n<br>" + resH
        h += "</td>"
        return h

    def resourceH(self) -> str:
        """ return html for this square's resource """
        h = ""
        for res in self.resources:
            h += res.a()
        return h


    def localMap(self, prox: int) -> str:
        """ a map centered around this square
        prox = number of squares distance to see
        """
        r, c = self.getCoords()
        rFrom = max(r - prox, 0)
        rTo = min(r + prox, config.NUM_ROWS - 1)
        rValues = list(range(rFrom, rTo+1))
        # cols wrap around, rows don't
        cValues = [c % config.NUM_COLS
                   for c in range(c-prox, c+prox+1)]
        h = "<table class='map'>\n"
        for row in rValues:
            h += "<tr>\n"
            for col in cValues:
                sq = self.theMap.squares[row][col]
                h += form("  {}\n", sq.tdh())
            #//for col
            h += "</tr>\n"
        #//for row
        h += "</table>\n"
        return h



#---------------------------------------------------------------------

def makeRandomSylable() -> str:
    """ make a random sylable for a name """
    s1 = random.choice("p b t d k g f v s z h".split() + [""]*2)
    s2 = random.choice("r y".split() + [""]*9)
    vowel = random.choice("i e a o u oi au".split())
    s3 = random.choice("p b t d k g f v s z".split() + [""]*9)
    syl = s1 + s2 + vowel + s3
    return syl

def makeRandomName() -> str:
    """ make a random name for a square """
    name = ""
    while True:
        name += makeRandomSylable()
        if len(name) >= random.randint(3,6): break
    #//while
    return name[0].upper() + name[1:]


#---------------------------------------------------------------------

class WorldMap:

    rows: int # number of rows in map
    cols: int # number of columns in map
    squares: list[list[Square]] = []
    resourceLocs: dict[str, list[Square]] = {}

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.squares = []
        for r in range(rows):
            theRow = []
            for c in range(cols):
                theRow.append(self.makeSquare(r, c))
            #//for c
            self.squares.append(theRow)
        #//for r
        self.allocateResources()
        self.listResources()

    def makeSquare(self, rix: int, cix: int) -> Square:
        """ make a random Square """
        wid = "%02d%02d" % (rix, cix)
        sq = Square(wid, self)
        if random.random() < 0.6:
            sq.isLand = False # make it sea
            sq.name = wid
        else:
            sq.name = makeRandomName()
        return sq

    def allocateResources(self):
        for sq in self.mySquares():
            if not sq.isLand: continue
            for _, res in sortedKv(resourceManager.data):
                if random.random() < res.probPc/100:
                    sq.resources += [res]
            #//for _,res
        #// for sq

    def mySquares(self) -> Iterator[Square]:
        for row in self.squares:
            for sq in row:
                yield sq


    def listResources(self):
        """ make a list of where the resources are, and put it
        in (resourceLocs).
        """
        for resId,_ in kv(resourceManager.data):
            self.resourceLocs[resId] = []
        #//for
        for sq in self.mySquares():
            for sqRes in sq.resources:
                self.resourceLocs[sqRes.wid].append(sq)
        #//for sq

    def squaresForResource(self, resId: str) -> list[Square]:
        return self.resourceLocs[resId]

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


worldMap = WorldMap(rows=config.NUM_ROWS, cols=config.NUM_COLS)

#---------------------------------------------------------------------

def randNames():
    print("some random names:")
    for i in range(10):
        print(makeRandomName())



#end
