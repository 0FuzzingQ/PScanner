# -*- coding: utf-8 -*-

import os
import subprocess
import threading
import sys
import datetime
from lib.param import get_param,analyse_param
from core.host import get_host
<<<<<<< HEAD
from lib.logging import info,test
=======
>>>>>>> 17d4fb4b69e75c9e75e43ab67f80c2694431dea6
#from core import port




def run():

<<<<<<< HEAD
    test()
    exit()

=======
>>>>>>> 17d4fb4b69e75c9e75e43ab67f80c2694431dea6
    target,speed,output = get_param()
    analyse_param(target,speed,output)
    target_list = analyse_target(target)

    get_host(target_list)



    
    

if __name__ == "__main__":
    run()



