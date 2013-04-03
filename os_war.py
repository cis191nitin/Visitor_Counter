#!/usr/bin/python
import sys
count_update = sys.argv[1]
if count_update == "mac":
        m_counter = open("mac.txt", 'a+')
        new_count  = int(m_counter.readlines()[-1].strip("\n")) + 1
        m_counter.write(str(new_count) + "\n")
        m_counter.close()
        print "A Silly Mac Fan boy"
elif count_update  == "windows":
        w_counter = open("windows.txt", 'a+')
        new_count  = int(w_counter.readlines()[-1].strip("\n")) + 1
        w_counter.write(str(new_count) + "\n")
        w_counter.close()
        print "One of Bill Gate's Exploits"
else:
        l_counter = open("linux.txt", 'a+')
        new_count  = int(l_counter.readlines()[-1].strip("\n")) + 1
        l_counter.write(str(new_count) + "\n")
        l_counter.close()
        print "A True Follower of Saint IGNUcis, All Hail!" 
