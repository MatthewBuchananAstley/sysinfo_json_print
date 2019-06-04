#!/usr/bin/env python3

import os,sys,re


itemarr = []
itemdict = dict()

def getmeminfo():

   meminfo = open("/proc/meminfo", "r") 
   pattern = re.compile("^MemFree|^MemTotal|^MemAvailable|^Cached")

   for item in meminfo:
      if pattern.search(item):	
         pat_rstrip = item.rstrip()
         #print("{0:s}".format(pat_rstrip))
         itemarr.append(pat_rstrip)
#   print(itemarr)


   for i in itemarr:
      (one,two,three) = i.split()
      #print(one,"=", two )
      itemdict[ one ] = two 

   #print(itemdict)
   return(itemdict) 
#getmeminfo() 
