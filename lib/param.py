# -*- coding: utf-8 -*-
import argparse

def get_param():
    print ("[*]For use info:python main.py -h,--help")

    parser = argparse.ArgumentParser(description='Scan Mission Params Needed')

    parser.add_argument('-t', help = "folders you want to scan" , dest = "input")
    parser.add_argument('-c', help = "scan speed [1,2,3]" , dest = "speed")
    parser.add_argument('-o', help = "result to save" ,  dest = "output")
    #parser.add_argument('-l', help = "log of relationship before file and watermark" , dest = "logpath")

    args = parser.parse_args()
    target = args.input
    speed = args.speed
    output = args.output

    return target,speed,output
    
def analyse_param(target,speed,output):

    try:
        with open(target,"w") as target_f:
            target_f.close()
    except:

        print("[!]找不到目标文件")

    try:
        with open(output,"w") as output_f:
            output_f.close()

    except:

        print("[!]无法创建结果文件")

    if speed not in [1,2,3]:

        print("[!]-c参数不正确，可选项[1，2，3]")
        exit()


def  analyse_target(target):

    try:

        with open(target,"r") as f:
            content = f.readlines()
            
            if len(content) == 0:
                print("[!]目标文件内容为空")
                exit()
            else:
                target_list = [x.strip("\n") for x in content]
                return target_list

    except:

        print("[!]目标读取失败")
    