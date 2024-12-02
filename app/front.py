# front.py = front page of website

import config
import allpages
from allpages import *

#---------------------------------------------------------------------

@app.route("/")
def index():
    return "this is the front page of Diplorisk"

#end
