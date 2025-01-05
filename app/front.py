# front.py = front page of website

from utils import butil
from utils.butil import form, kv, sortedKv

import config
import allpages
from allpages import *

import worldmap
from worldmap import worldMap
import resource
from resource import Resource, resourceManager

#---------------------------------------------------------------------

@app.route("/")
def index():
    tem = jinjaEnv.get_template("front.html")
    h = tem.render()
    return h

#---------------------------------------------------------------------

@app.route("/map")
def drawMap():
    tem = jinjaEnv.get_template("map.html")
    h = tem.render(
        #theMap = "",
        theMap = worldMap.h(),
    )
    return h

#---------------------------------------------------------------------

@app.route("/w/square/<wid>")
def drawSquare(wid: str):
    sq: Square = worldmap.squares.data[wid]
    tem = jinjaEnv.get_template("square.html")
    h = tem.render(
        sq = sq,
    )
    return h

#---------------------------------------------------------------------

@app.route("/resources")
def listResources():
    tem = jinjaEnv.get_template("resources.html")
    h = tem.render(
        resourceTable = resourceTable()
    )
    return h

def resourceTable() -> str:
    """ a table of resources """
    h = """<table class='report_table'>
        <tr>
            <th>Wid</th>
            <th>Name</th>
            <th>fcol</th>
            <th>bcol</th>
            <th>blurb</th>
        </tr>"""
    for wid, r in sortedKv(resource.resourceManager.data):
        h += form("""
            <tr>
                <td>{wid}</td>
                <td>{name}</td>
                <td><tt>{fcol}</tt></td>
                <td><tt>{bcol}</tt></td>
                <td>(blurb)</td>
            </tr>
""",
            wid = r.a(),
            name = r.aName(),
            fcol = r.fcol,
            bcol = r.bcol
)
    #//for wid, r
    h += "</table>\n"
    return h

#---------------------------------------------------------------------

@app.route("/w/resource/<wid>")
def drawResource(wid: str):
    res: Resource = resourceManager.data[wid]
    numLoc = len(worldMap.squaresForResource(res.wid))
    tem = jinjaEnv.get_template("resource.html")
    h = tem.render(
        wid = wid,
        widName = res.widName(),
        numLoc = numLoc,
        sqTable = sqTable(res)
    )
    return h

def sqTable(res: Resource) -> str:
    """ return a table of squares containing a resource """
    h = """<table class='report_table'>
        <tr>
            <th>Location</th>
            <th>Name</th>
            <th>Resources</th>
        </tr>"""
    resId = res.wid
    for sq in worldMap.squaresForResource(resId):
        h += form("""
            <tr>
                <td>{wid}</td>
                <td>{sqName}</td>
                <td>{sqRes}</td>
            </tr>
""",
            wid = sq.a(),
            sqName = sq.name,
            sqRes = sq.resourceH()
)
    #//for
    h += "</table>\n"
    return h



#---------------------------------------------------------------------

#end
