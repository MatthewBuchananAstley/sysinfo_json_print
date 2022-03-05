#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# FileCopyrightText: <text> 2019 - 2022 Matthew Buchanan Astley (matthewbuchanan@astley.nl) </text> 

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
