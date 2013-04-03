#!/usr/bin/python
counter = open("count.txt", 'a+')
new_count  = int(counter.readlines()[-1].strip("\n")) + 1
counter.write(str(new_count) + "\n")
counter.close()
      
