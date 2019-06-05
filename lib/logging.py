# -*- coding: utf-8 -*-
import os


def info(content):

    path = os.getcwd() + "/log/log.txt"

    try:
        print(content)
        with open(path,"a") as f:

            f.write(content + "\n")
        f.close()

    except:

        pass

def test():

    open("./requirements.txt")

