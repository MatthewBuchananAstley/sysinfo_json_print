#!/usr/bin/env python3
#
# SPDX-License-Identifier: GPL-3.0-or-later
# FileCopyrightText: <text> 2019 - 2022 Matthew Buchanan Astley (matthewbuchanan@astley.nl) </text> 

import os,sys,posix
import cpuinfo
import meminfo
import json

nesteddict = {} 

#print("\r")
unameinf = os.uname()
unamesysname = unameinf.sysname
unamenodename = unameinf.nodename
unamerelease = unameinf.release
unameversion = unameinf.version
unamemachine = unameinf.machine

cpu_count = posix.cpu_count()

#print("\r")
#print("sysname  =", unamesysname)
#print("nodename =", unamenodename)
#print("release  =", unamerelease)
#print("version  =", unameversion)
#print("machine  =", unamemachine)

nesteddict = dict({ 'sysinfo' : { 'sysname' : unamesysname, 'nodename' : unamenodename, 'release' : unamerelease, 'version' : unameversion, 'machine' : unamemachine } } ) 


#print(nesteddict)

#print("\r")
#print("Number of CPU's = ",cpu_count,"\n")
#print("Cpu:")

cpinfo = cpuinfo.getcpuinfo()

nesteddict['sysinfo'][ 'cpuinfo' ] = cpinfo
nesteddict['sysinfo'][ 'cpucount' ] = cpu_count 

#print(cpinfo)
#print("\r")
#print("\r")
#print("Memory:")
#print("\r")

meminf = meminfo.getmeminfo()

nesteddict['sysinfo']['meminfo'] = meminf

def printinf():

    print(json.dumps(nesteddict,sort_keys=True, indent=4))


printinf()

#dirlist = posix.listdir(path="./")
#for file in dirlist:
#   statfile = os.stat(file)
#   print(file,statfile.st_ctime)

