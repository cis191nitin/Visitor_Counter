#!/usr/bin/python
m_counter = open("mac.txt", 'rw')
m_lastline = m_counter.readlines()[-1].strip("\n")
m_counter.close()
w_counter = open("windows.txt", 'rw')
w_lastline = w_counter.readlines()[-1].strip("\n")
w_counter.close()
l_counter = open("linux.txt", 'rw')
l_lastline = l_counter.readlines()[-1].strip("\n")
l_counter.close()
counts = [m_lastline, w_lastline, l_lastline]
print " ".join(counts)
