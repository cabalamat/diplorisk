# resource.py = resources

"""

For historical info on resources, see
https://www.reddit.com/r/AskHistorians/comments/8bl5lu/what_raw_materials_were_most_important_to_a_ww2/
"""

from utils import butil
from utils.butil import form

import wentity

import config


#---------------------------------------------------------------------

class Resource(wentity.WEntity):
    """ a resource that some squares can have """


    wid: str # web id
    name: str = "" # name of this resource
    fcol: str # foreground colour (includes preceeding #)
    bcol: str # background colour (includes preceeding #)
    blurb: str = "" # description of this resource

    prob: float = 0.1 # probability that a sq will have it


    def __init__(self, wid):
        self.wid = wid

    @classmethod
    def entityType(cls) -> str:
        return "resource"

    def icon(self)-> str:
        return "<i class='fas fa-cubes'></i> "

    def widName(self):
        h = form("<b "
            "style='color:{fcol};background:{bcol};padding: 2px 4px'"
            ">{wid}</b> {name}",
            fcol=self.fcol,
            bcol=self.bcol,
            wid=self.wid,
            name=self.name)
        return h

    def a(self) -> str:
        h = form("<a href='{url}' "
            "style='color:{fcol};background:{bcol};padding: 2px 4px'>"
            "<b>{wid}</b></a>",
            url=self.url(),
            fcol=self.fcol,
            bcol=self.bcol,
            wid=self.wid)
        return h


#---------------------------------------------------------------------

"""
These are:
wid:name:fcol:bcol
blurb
"""

RESOURCES = """\
C:Coal:        ffffff:000000:10
Fe:Iron:       ffdddd:662222:10
oil:Oil:       99ff99:224422:10
Al:Aluminium:  440000:eebbbb:10
Cu:Copper:     004400:99ff99:10
Zn:Zinc:       000000:eeeeee:10
Sn:Tin:        000000:cccccc:10
rub:Rubber:    eeddbb:332200:10
W:Tungsten:    220088:bbaacc:10
Mn:Manganese:  001166:ccddff:10
Cr:Chromium:   ffffff:660088:10
"""

resourceManager = wentity.WEntityManager("resource")

res = RESOURCES.strip().splitlines()
for rLine in res:
    w, n, fc, bc, prob = rLine.split(":")
    r = Resource(w)
    r.name = n.strip()
    r.fcol = "#" + fc.strip()
    r.bcol = "#" + bc.strip()
    r.prob = float(prob.strip())/100
    r.blurb = ""
    resourceManager.add(r)
#//for rLine




#end
