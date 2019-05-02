#!/usr/bin/python2
import socket
import numpy as np

import re
import urllib
from time import sleep
import matplotlib as mpl
from matplotlib import pyplot as plt

plt.ion()
mpl.rcParams['toolbar']='None'
fig = plt.figure(figsize=(10,5))

ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
temp = []
pre = []
hum = []
all_data = []
host = '192.168.1.100'
port = 5000

s = socket.socket()
s.bind((host, port))

s.listen(1)
c, addr = s.accept()

print ("Connection from: " + str(addr))
while True:
    data = c.recv(1024)
    data_str = data.decode('utf-8')
    all_data = data_str.split()
    temp.append(float(all_data[1]))
    pre.append(round(float(all_data[2]),2))
    hum.append(float(all_data[3]))
    if len(temp)>10:
	   temp.pop(0)
        pre.pop(0)
	   hum.pop(0)
	#l = temprPlot.pop(0)
	#l.remove()
    
    plt.subplot(3,1,1) 
    plt.cla()   
    plt.xlabel("time/seconds")
    plt.ylabel("temperature/C")
    temprPlot = ax1.plot(temp,'b-')

    
    plt.subplot(3,1,2) 
    plt.cla()   
    plt.xlabel("time/seconds")
    plt.ylabel("pressure/atm")
    prePlot = ax2.plot(pre,'r--')
    ax2.ticklabel_format(useOffset=False, style='plain')

    
    plt.subplot(3,1,3) 
    plt.cla()   
    plt.xlabel("time/seconds")
    plt.ylabel("humidity/%")
    humPlot = ax3.plot(hum,'k:')
 
    fig.canvas.draw()
    if not data:
         break
    print ("from connected user: " + data_str)
    #myfile = open('weather.txt','a')
    #myfile.write(data_str)
    #myfile.write('\n')
    #myfile.close()
    #data = str(data).upper()
    print ("sending: " + str(data))
    #c.send(data)
s.close()
