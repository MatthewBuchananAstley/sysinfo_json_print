#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# FileCopyrightText: <text> 2019 - 2022 Matthew Buchanan Astley (matthewbuchanan@astley.nl) </text> 

import os,sys,re

def getcpuinfo():
   cpuinfo = open("/proc/cpuinfo", "r") 
   itemarr = []
   pattern = re.compile("^model name|^cache size")

   for item in cpuinfo:
      if pattern.search(item):	
         pat_rstrip = item.rstrip()
         #print("{0:s}".format(pat_rstrip))
         itemarr.append( pat_rstrip )
         
   return(itemarr)

