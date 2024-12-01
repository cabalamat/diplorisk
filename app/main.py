# main.py = main module for Diplorisk

import argparse

from flask import request, redirect

from utils.butil import prn

import allpages
from allpages import *

import config

# pages:
import front

#---------------------------------------------------------------------

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="""\
Start Diplorisk
""")
    parser.add_argument("-d", "--debug",
        help="Run in debugging mode",
        action="store_true")
    parser.add_argument("-p", "--port",
        help="Port number to use",
        type=int,
        default=config.PORT)
    parser.add_argument("-v", "--verbose",
        help="Make output more verbose",
        action="store_true")
    commandLineArgs = parser.parse_args()
    prn("commandLineArgs=%r" % (commandLineArgs,))
    host = "127.0.0.1" if commandLineArgs.debug else "0.0.0.0"

    app.run(host=host,
        port=commandLineArgs.port,
        debug=commandLineArgs.debug)
    #print("Starting Diplorisk...")



#end
