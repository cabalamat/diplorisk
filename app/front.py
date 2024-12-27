# front.py = front page of website

import config
import allpages
from allpages import *

#---------------------------------------------------------------------

@app.route("/")
def index():
    tem = jinjaEnv.get_template("front.html")
    h = tem.render()
    return h

#end
