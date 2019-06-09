# -*- coding: utf-8 -*-

import os
import subprocess
import threading
import sys
import datetime
from lib.param import get_param,analyse_param,analyse_target
from core.host import get_host
from lib.logging import info,test
#from core import port




def run():

    #test()
    #exit()

    target,speed,output = get_param()
    analyse_param(target,speed,output)
    target_list = analyse_target(target)

    #print(target_list)

    get_host(target_list)



    
    

if __name__ == "__main__":
    run()



