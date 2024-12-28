# wentity.py = web entity

"""
A Web Entity (instance of WEntity subclass) is an object that has
a url associated with it.

"""

from typing import Optional

from utils import butil
from utils.butil import form

#---------------------------------------------------------------------

class WEntityManager:
    """ manages web entities """

    entityTyp: str # entity type
    data: dict[str, 'WEntity'] = {}

    def __init__(self, enTyp: str):
        self.data = {}
        self.entityTyp = enTyp

    def add(self, wen: 'WEntity'):
        self.data[wen.wid] = wen



#---------------------------------------------------------------------

class WEntity:

    def a(self) -> str:
        """ return HTML for an a href to the entity """
        h = form("<a href='{u}'>{w}</a>",
                 u=self.url(),
                 w=self.getWid())
        return h

    def url(self) -> str:
        """ return the entity's url """
        u = form("/w/{}/{}", self.entityType(), self.getWid())
        return u

    def getWid(self) -> str:
        """ return the entity's web id """
        return self.wid

    @classmethod
    def entityType(cls) -> str:
        """ must be implemented by subclass """
        raise ImplementedBySubclass


#---------------------------------------------------------------------


#end
