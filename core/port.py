# -*- coding: utf-8 -*-
from lib.logging import info
import time
import subprocess
import threading
from libnmap.parser import NmapParser
import pandas as pd

def get_port(target):
    
    host_path = "./output/hosts/" + target.split("/")[0]
    output_path = "./output/ports/" + target.split("/")[0]

    try:
        cmd = "sudo masscan -iL %s.txt  -oL %s --rate=10000" % (host_path,output_path)
        info("[!]端口扫描线程开启  任务名 : %s" % cmd)
        subprocess.check_call(cmd)
        info("[!]端口扫描线程开启  任务名 : %s" % cmd)
    except:
        #print("[!]文件打开扫描异常: %s " % host_path)
        info("[!]端口扫描异常: %s " % target)

    with open(output_path,"r") as f:

        
        content = f.readlines()
        portdict = {}
        data = []
        for i in content:
            if "#" in i:
                continue
            else:
                port = i.strip("\n").split(" ")[2]
                host = i.strip("\n").split(" ")[3]
                if host not in portdict.keys():
                    portdict[host] = [port]
                else:
                    portdict[host].append(port)
        for i in portdict.keys():
            data.append(portdict[i] + [i])
    f.close()

    nmap_scan_thread = []
    
    if len(data) <= 8:
        for i in range(0,len(data)):
            t = threading.Thread(target=scan_service, args=(data[i], i+1,))
            nmap_scan_thread.append(t)
            t.start()
    
    else:

        infest = int(len(data)/4)

        t1 = threading.Thread(target = scan_service, args =(data[:infest],1,))
        t2 = threading.Thread(target = scan_service, args =(data[infest:infest*2],2,))
        t3 = threading.Thread(target = scan_service, args =(data[infest*2:infest*3],3,))
        t4 = threading.Thread(target = scan_service, args =(data[infest*3:],4,))

        nmap_scan_thread.append(t1)
        nmap_scan_thread.append(t2)
        nmap_scan_thread.append(t3)
        nmap_scan_thread.append(t4)

        t1.start()
        t2.start()
        t3.start()
        t4.start()

def scan_service(data,id):

    for i in data:
        ports = ','.join(x for x in i[:-1])
        cmd = "nmap -sV %s -p%s -oX %s.xml" %(i[-1],ports,"./output/services/" + i[-1])
        info("[!]服务扫描线程开启 线程号: %s 任务名 : %s" %(str(id),cmd))
        subprocess.check_call(cmd,shell=True)
        info("[*]服务扫描线程完成 线程号: %s 任务名 : %s" %(str(id),cmd))
        nmap_report = NmapParser.parse_fromfile("./output/services/" + i[-1] + ".xml")
        res = [ [a.address,b.port,b.service,b.banner] for a in nmap_report.hosts for b in a.services  ]
        #print(res)

        pd.DataFrame(res,columns=['ip','port','server','banner'])

        res.to_csv("./output/results.csv",header=False,mode="a")

        



        






