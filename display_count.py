#!/usr/bin/python
counter = open("count.txt", 'rw')
lastline = counter.readlines()[-1].strip("\n")
counter.close()
print lastline

