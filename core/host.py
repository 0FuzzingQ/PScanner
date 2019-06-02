# -*- coding: utf-8 -*-
import threading
def get_host(target_list):
    
    host_scan_thread = []

    if len(target_list) < 4:

        for target in target_list:

            t = Thread(target = scan_host, args =(target,))
            host_scan_thread.append(t)
            t.start()
    
    else:

        infest = int(len(target_list)/4)

        t1 = Thread(target = scan_host, args =(target_list[:infest],))
        t2 = Thread(target = scan_host, args =(target_list[infest:infest*2],))
        t3 = Thread(target = scan_host, args =(target_list[infest*2:infest*3],))
        t4 = Thread(target = scan_host, args =(target_list[infest*3:],))

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



            