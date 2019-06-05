# -*- coding: utf-8 -*-
import threading
import subprocess
from lib.logging import info
from core.port import get_port

def get_host(target_list):
    
    host_scan_thread = []

    if len(target_list) < 4:

        for i in range(0,len(target_list)):

            t = threading.Thread(target = scan_host, args =(target_list[i],i+1,))
            host_scan_thread.append(t)
            t.start()
    
    else:

        infest = int(len(target_list)/4)

        t1 = threading.Thread(target = scan_host, args =(target_list[:infest],1,))
        t2 = threading.Thread(target = scan_host, args =(target_list[infest:infest*2],2,))
        t3 = threading.Thread(target = scan_host, args =(target_list[infest*2:infest*3],3,))
        t4 = threading.Thread(target = scan_host, args =(target_list[infest*3:],4,))

        host_scan_thread.append(t1)
        host_scan_thread.append(t2)
        host_scan_thread.append(t3)
        host_scan_thread.append(t4)

        t1.start()
        t2.start()
        t3.start()
        t4.start()

    while True:
        thread_count = 0
        for t in host_scan_thread:

            if t.isAlive():
                thread_count = thread_count + 1

        if thread_count == 0:

            pass



def scan_host(targets,id):

    #print("[!]线程开启 线程号 :%s " % str(id))
    info("[!]主机扫描线程开启 线程号 :%s " % str(id))

    if len(targets) == 1:
        try:
            cmd = "fping -g %s -a > %s.txt" %(targets,"./output/hosts/" + targets.split("/")[0])
            info("[!]主机扫描线程开启 线程号 :%s 任务名 :%s " % (str(id),cmd))
            subprocess.check_call(cmd,shell=True)
            info("[!]主机扫描线程报错 线程号 :%s 任务名 :%s " % (str(id),cmd))
            get_port(targets)

        except:
            #print("[!]线程报错 线程号 :%s 任务名 :%s " % (str(id),cmd))
            info("[!]主机扫描线程报错 线程号 :%s 任务名 :%s " % (str(id),cmd))
    else:
        for t in targets:
            try:
                cmd = "fping -g %s -a > %s.txt" %(t,"./output/hosts/" + t.split("/")[0])
                info("[!]主机扫描线程开启 线程号 :%s 任务名 :%s " % (str(id),cmd))
                subprocess.check_call(cmd,shell=True)
                info("[!]主机扫描线程报错 线程号 :%s 任务名 :%s " % (str(id),cmd))
                get_port(targets)
            except:
                #print("[!]线程报错 线程号 :%s 任务名 :%s " % (str(id),cmd))
                info("[!]主机扫描线程报错 线程号 :%s 任务名 :%s " % (str(id),cmd))





