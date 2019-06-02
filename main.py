# -*- coding: utf-8 -*-

import os
import subprocess
import threading
import sys
import datetime
from lib.param import get_param,analyse_param
from core.host import get_host
#from core import port




def run():

    target,speed,output = get_param()
    analyse_param(target,speed,output)
    target_list = analyse_target(target)

    get_host(target_list)



    
    

if __name__ == "__main__":
    run()



