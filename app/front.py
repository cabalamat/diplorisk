# front.py = front page of website

import config
import allpages
from allpages import *

import worldmap

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
        theMap = worldmap.worldMap.h(),
    )
    return h

#---------------------------------------------------------------------

@app.route("/w/square/<wid>")
def drawSquare(wid: str):
    sq: Square = worldmap.squares.data[wid]
    tem = jinjaEnv.get_template("square.html")
    h = tem.render(
        sq = sq,
        localMap = None,
    )
    return h


#---------------------------------------------------------------------

#end
